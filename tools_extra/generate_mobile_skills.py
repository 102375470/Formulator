from tqdm import tqdm

from kungfus import SUPPORT_KUNGFU
from tools import *
from tools.generate_skills import prepare_lua_engine, execute_lua, INCLUDE_LUA


def prepare_skills():
    skills = []
    for kungfu in SUPPORT_KUNGFU.values():
        for skill_id in kungfu.skills:
            skill_id = abs(skill_id)
            if skill_id in skills:
                continue
            skills.append(skill_id)
    return skills


ATTRIBUTE_TYPE = {
    "CALL_PHYSICS_DAMAGE": "physical_damage_call",
    "CALL_LUNAR_DAMAGE": "lunar_damage_call",
    "CALL_SOLAR_DAMAGE": "solar_damage_call",
    "CALL_NEUTRAL_DAMAGE": "neutral_damage_call",
    "CALL_POISON_DAMAGE": "poison_damage_call",

    "CALL_ADAPTIVE_DAMAGE": "adaptive_damage_call",

    "CALL_SURPLUS_PHYSICS_DAMAGE": "physical_surplus_call",
    "CALL_SURPLUS_LUNAR_DAMAGE": "lunar_surplus_call",
    "CALL_SURPLUS_SOLAR_DAMAGE": "solar_surplus_call",
    "CALL_SURPLUS_NEUTRAL_DAMAGE": "neutral_surplus_call",
    "CALL_SURPLUS_POISON_DAMAGE": "poison_surplus_call"
}
ATTRIBUTE_TYPE_CODE = "\n".join(f'{k}={i},' for i, k in enumerate(ATTRIBUTE_TYPE))
ATTRIBUTE_TYPE_MAP = {i: v for i, v in enumerate(ATTRIBUTE_TYPE.values())}
INCLUDE_LUA = INCLUDE_LUA + """
SKILL_KIND_TYPE = {
    PHYSICS = 0,
    SOLAR_MAGIC = 1,
    LUNAR_MAGIC = 2,
    NEUTRAL_MAGIC = 3,
    POISON = 4,
};
PLAYER_ARENA_TYPE = {
    DPS = 0,
    T = 1,
    THERAPY = 2
};
""" + f"""
ATTRIBUTE_TYPE = {{
{ATTRIBUTE_TYPE_CODE}
}};
"""

SKILL_TAB = read_tab("settings/skill_mobile/skills.tab")
SKILL_TXT = read_tab("ui/Scheme/case_mobile/skill.txt")

SCRIPTS_PATH = "scripts/skill_mobile"


class SkillLua:
    skill_id = 0
    skill_level = 0
    skill_name = ""
    alias_name = ""

    platform = 0

    kind_type = None
    recipe_type = None
    recipe_mask = None
    event_mask_1 = 0
    event_mask_2 = 0

    weapon_damage_cof = 0

    physical_damage_call = 0
    lunar_damage_call = 0
    solar_damage_call = 0
    neutral_damage_call = 0
    poison_damage_call = 0
    adaptive_damage_call = 0

    physical_surplus_call = 0
    lunar_surplus_call = 0
    solar_surplus_call = 0
    neutral_surplus_call = 0
    poison_surplus_call = 0

    @property
    def damage_call(self):
        return self.physical_damage_call + self.lunar_damage_call + self.solar_damage_call + self.neutral_damage_call + self.poison_damage_call + self.adaptive_damage_call

    @property
    def surplus_call(self):
        return self.physical_surplus_call + self.lunar_surplus_call + self.solar_surplus_call + self.neutral_surplus_call + self.poison_surplus_call

    @staticmethod
    def empty_function(*args):
        return

    def __init__(
            self, skill_id, skill_level, skill_name, kind_type,
            weapon_request, skill_cof, dot_cof, surplus_cof
    ):
        self.skill_id = skill_id
        self.skill_level = skill_level
        if skill_name:
            self.skill_name = skill_name
        self.kind_type = kind_type
        self.weapon_request = weapon_request
        if weapon_request:
            self.weapon_damage_cof = 1024
        self.skill_cof = skill_cof
        self.dot_cof = dot_cof
        self.surplus_cof = surplus_cof

    def __getitem__(self, key):
        if key in dir(self):
            return getattr(self, key)
        else:
            return self.empty_function

    def __setitem__(self, key, value):
        if key in dir(self):
            setattr(self, key, value)

    @property
    def dwSkillID(self):
        return self.skill_id

    @dwSkillID.setter
    def dwSkillID(self, dwSkillID):
        self.skill_id = dwSkillID

    @property
    def dwLevel(self):
        return self.skill_level

    @dwLevel.setter
    def dwLevel(self, dwLevel):
        self.skill_level = dwLevel

    @property
    def nWeaponDamagePercent(self):
        return self.weapon_damage_cof

    @nWeaponDamagePercent.setter
    def nWeaponDamagePercent(self, nWeaponDamagePercent):
        if self.weapon_request:
            self.weapon_damage_cof = nWeaponDamagePercent

    def AddAttribute(self, *args):
        if len(args) < 3:
            return

        attr_type = args[1]
        if attr := ATTRIBUTE_TYPE_MAP.get(attr_type):
            if "call" in attr:
                setattr(self, attr, getattr(self, attr) + 1)
            elif "adaptive" in attr:
                setattr(self, attr, args[3])
            else:
                setattr(self, attr, args[2])

    def __call__(self, *args, **kwargs):
        pass


def parse_lua(skill_id):
    skill_row = SKILL_TAB[SKILL_TAB.SkillID == skill_id].iloc[0]
    alias_name = skill_row.SkillName
    max_level = int(skill_row.MaxLevel)
    kind_type = skill_row.KindType if pd.notna(skill_row.KindType) else ""
    weapon_request = int(skill_row.WeaponRequest)
    skill_cof = int(skill_row.SkillCoefficient) if pd.notna(skill_row.SkillCoefficient) else 0
    dot_cof = int(skill_row.DotCoefficient) if pd.notna(skill_row.DotCoefficient) else 0
    surplus_cof = int(skill_row.SurplusCoefficient) if pd.notna(skill_row.SurplusCoefficient) else 0
    lua_path = skill_row.ScriptFile.replace('\\', '/')
    skill_args = (
        kind_type, weapon_request, skill_cof, dot_cof, surplus_cof
    )
    return alias_name, max_level, lua_path, skill_args


def get_lua_path_name(x):
    try:
        return x.split("/")[1].split("_")[1]
    except:
        return x

def collect_result():
    result = []
    lua_engine = prepare_lua_engine(INCLUDE_LUA)
    for skill_id in tqdm(SKILL_TAB.SkillID):
        alias_name, max_level, lua_path, skill_args = parse_lua(skill_id)
        if "Default" in lua_path:
            continue

        filter_skill_txt = SKILL_TXT[SKILL_TXT.SkillID == skill_id]

        execute_lua(lua_engine, os.path.join(BASE_DIR, SCRIPTS_PATH, lua_path))
        if filter_skill_txt.empty:
            skill_name = None
        else:
            skill_name = filter_skill_txt.iloc[-1].Name

        skill = SkillLua(skill_id, 1, skill_name, *skill_args)
        skill.alias_name = alias_name
        skill.max_level = max_level
        skill.lua_path = get_lua_path_name(lua_path)
        lua_engine.globals()['GetSkillLevelData'](skill)

        if not skill.damage_call:
            del skill.skill_cof
        if not skill.surplus_call and skill.surplus_cof:
            del skill.surplus_cof
        if not skill.physical_damage_call and skill.weapon_damage_cof:
            del skill.weapon_damage_cof
        if not skill.damage_call and not skill.surplus_call and not skill.dot_cof:
            continue

        del skill.weapon_request
        if not skill.dot_cof:
            del skill.dot_cof
        result.append(vars(skill).copy())
    df = pd.DataFrame(result)
    return df


def generate():
    df = collect_result()
    df = df[[
        'skill_id', 'skill_name', 'alias_name', "lua_path", 'kind_type',
        'weapon_damage_cof', 'skill_cof', 'surplus_cof', 'dot_cof'
    ]]
    df.to_csv("assets/mobile_skills.csv", index=False)


if __name__ == '__main__':
    generate()
