import os
from dataclasses import dataclass
from typing import Type, Dict, List

from base.attribute import Attribute
from base.buff import Buff
from base.skill import Skill
# from general.gains import equipment

from schools import first

""" Directory """
# ASSETS_DIR = os.path.join(os.getcwd(), "qt/assets")
ASSETS_DIR = "qt/assets"
EQUIPMENTS_DIR = os.path.join(ASSETS_DIR, "equipments")
ENCHANTS_DIR = os.path.join(ASSETS_DIR, "enchants")
STONES_DIR = os.path.join(ASSETS_DIR, "stones.json")

""" Equipments """
POSITION_MAP = {
    '帽子': 'hat',
    '上衣': 'jacket',
    '腰带': 'belt',
    '护腕': 'wrist',
    '下装': 'bottoms',
    '鞋子': 'shoes',
    '项链': 'necklace',
    '腰坠': 'pendant',
    '戒指1': 'ring',
    '戒指2': 'ring',
    '远程武器': 'tertiary_weapon',
    '近战武器': 'primary_weapon',
    '额外武器': 'secondary_weapon'
}
STONES_POSITIONS = ["primary_weapon", 'secondary_weapon']
EMBED_POSITIONS = {
    "hat": 2,
    "jacket": 2,
    "belt": 2,
    "wrist": 2,
    "bottoms": 2,
    "shoes": 2,
    "necklace": 1,
    "pendant": 1,
    "ring": 0,
    "tertiary_weapon": 1,
    "primary_weapon": 3,
    "secondary_weapon": 3
}
SPECIAL_ENCHANT_POSITIONS = ["hat", "jacket", "belt", "wrist", "shoes"]
""" Attrs """
ATTR_TYPE_MAP = {
    "atMeleeWeaponDamageBase": "weapon_damage_base",
    "atMeleeWeaponDamageRand": "weapon_damage_rand",
    "atBasePotentialAdd": "all_major_base",
    "atAgilityBase": "agility_base",
    "atStrengthBase": "strength_base",
    "atSpiritBase": "spirit_base",
    "atSpunkBase": "spunk_base",
    "atPhysicsAttackPowerBase": "physical_attack_power_base",
    "atMagicAttackPowerBase": "magical_attack_power_base",
    "atLunarAttackPowerBase": "magical_attack_power_base",
    "atSolarAttackPowerBase": "magical_attack_power_base",
    "atSolarAndLunarAttackPowerBase": "magical_attack_power_base",
    "atPhysicsOvercomeBase": "physical_overcome_base",
    "atMagicOvercome": "magical_overcome_base",
    "atLunarOvercomeBase": "magical_overcome_base",
    "atSolarOvercomeBase": "magical_overcome_base",
    "atSolarAndLunarOvercomeBase": "magical_overcome_base",
    "atAllTypeCriticalStrike": "all_critical_strike_base",
    "atPhysicsCriticalStrike": "physical_critical_strike_base",
    "atMagicCriticalStrike": "magical_critical_strike_base",
    "atLunarCriticalStrike": "magical_critical_strike_base",
    "atSolarCriticalStrike": "magical_critical_strike_base",
    "atSolarAndLunarCriticalStrike": "magical_critical_strike_base",
    "atAllTypeCriticalDamagePowerBase": "all_critical_power_base",
    "atPhysicsCriticalDamagePowerBase": "physical_critical_power_base",
    "atMagicCriticalDamagePowerBase": "magical_critical_power_base",
    "atLunarCriticalDamagePowerBase": "magical_critical_power_base",
    "atSolarCriticalDamagePowerBase": "magical_critical_power_base",
    "atSolarAndLunarCriticalDamagePowerBase": "magical_critical_power_base",
    "atSurplusValueBase": "surplus",
    "atStrainBase": "strain_base",
    "atHasteBase": "haste_base",
}
ATTR_TYPE_TRANSLATE = {
    "weapon_damage_base": "基础武器伤害",
    "weapon_damage_rand": "浮动武器伤害",
    "all_major_base": "全属性",
    "agility_base": "身法",
    "strength_base": "力道",
    "spirit_base": "根骨",
    "spunk_base": "元气",
    "physical_attack_power_base": "外功攻击",
    "magical_attack_power_base": "内功攻击",
    "physical_critical_strike_base": "外功会心",
    "magical_critical_strike_base": "内功会心",
    "all_critical_strike_base": "全会心",
    "physical_critical_power_base": "外功会效",
    "magical_critical_power_base": "内功会效",
    "all_critical_power_base": "全会效",
    "physical_overcome_base": "外功破防",
    "magical_overcome_base": "内功破防",
    "surplus": "破招",
    "strain_base": "无双",
    "haste_base": "加速",
}
ATTR_TYPE_TRANSLATE_REVERSE = {v: k for k, v in ATTR_TYPE_TRANSLATE.items()}
STONE_ATTR = [
    "atMeleeWeaponDamageBase", "atSurplusValueBase", "atStrainBase", "atHasteBase",
    "atAllTypeCriticalStrike", "atAllTypeCriticalDamagePowerBase",
    "atAgilityBase", "atStrengthBase", "atSpiritBase", "atSpunkBase",
    "atPhysicsAttackPowerBase", "atPhysicsCriticalStrike",
    "atPhysicsCriticalDamagePowerBase", "atPhysicsOvercomeBase",
    "atMagicAttackPowerBase", "atMagicCriticalStrike",
    "atMagicCriticalDamagePowerBase", "atMagicOvercome"
]

""" Top """


@dataclass
class School:
    school: str
    major: str
    kind: str
    attribute: Type[Attribute]
    formation: str
    talents: List[Dict[int, Buff]]
    skills: Dict[int, Skill]
    buffs: Dict[int, Buff]


SUPPORT_SCHOOL = {
    10464: School(
        school="霸刀",
        major="力道",
        kind="外功",
        attribute=first.BeiAoJue,
        formation="霜岚洗锋阵",
        talents=first.TALENTS,
        skills=first.SKILLS,
        buffs=first.BUFFS
    )
}

""" Equip """

MAX_EMBED_ATTR = 3
MAX_BASE_ATTR = 6
MAX_MAGIC_ATTR = 12
MAX_ENCHANT_ATTR = 4
MAX_STONE_ATTR = 3

MAX_EMBED_LEVEL = 8
MAX_STRENGTH_LEVEL = 8
MAX_STONE_LEVEL = 6


def EMBED_COF(level):
    if level > 6:
        return (level * 0.65 - 3.2) * 1.3
    else:
        return level * 0.195


def STRENGTH_COF(level):
    return level * (0.7 + 0.3 * level) / 200


# EQUIP_GAINS_NAME = {
#     **equipment.EQUIP_GAINS_NAME,
#     **wen_shui_jue.EQUIP_GAINS_NAME,
#     **bei_ao_jue.EQUIP_GAINS_NAME,
#     **bing_xin_jue.EQUIP_GAINS_NAME,
#     **yi_jin_jing.EQUIP_GAINS_NAME,
#     **ao_xue_zhan_yi.EQUIP_GAINS_NAME,
#     **gu_feng_jue.EQUIP_GAINS_NAME,
#     **fen_ying_sheng_jue.EQUIP_GAINS_NAME
# }
# EQUIP_GAINS = {
#     **equipment.EQUIP_GAINS,
#     **wen_shui_jue.EQUIP_GAINS,
#     **bei_ao_jue.EQUIP_GAINS,
#     **bing_xin_jue.EQUIP_GAINS,
#     **yi_jin_jing.EQUIP_GAINS,
#     **ao_xue_zhan_yi.EQUIP_GAINS,
#     **gu_feng_jue.EQUIP_GAINS,
#     **fen_ying_sheng_jue.EQUIP_GAINS
# }

""" Talent """
MAX_TALENTS = 12

# TALENT_GAINS = {
#     **wen_shui_jue.TALENT_GAINS,
#     **bei_ao_jue.TALENT_GAINS,
#     **bing_xin_jue.TALENT_GAINS,
#     **yi_jin_jing.TALENT_GAINS,
#     **ao_xue_zhan_yi.TALENT_GAINS,
#     **gu_feng_jue.TALENT_GAINS,
#     **fen_ying_sheng_jue.TALENT_GAINS
# }

""" Recipes """
MAX_RECIPE_SKILLS = 12
MAX_RECIPES = 4

# RECIPE_GAINS = {
#     **wen_shui_jue.RECIPE_GAINS,
#     **bei_ao_jue.RECIPE_GAINS,
#     **bing_xin_jue.RECIPE_GAINS,
#     **yi_jin_jing.RECIPE_GAINS,
#     **ao_xue_zhan_yi.RECIPE_GAINS,
#     **gu_feng_jue.RECIPE_GAINS,
#     **fen_ying_sheng_jue.RECIPE_GAINS
# }
