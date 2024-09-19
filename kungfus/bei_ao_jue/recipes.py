from general.recipes import *


class 上将军印无视外防(PhysicalShieldGainRecipe):
    value = -205

    def add_skill(self, skill: Skill):
        if skill.skill_id in (16800, 16801, 16802, 16803, 16804, 17043, 19423, 19424):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (16800, 16801, 16802, 16803, 16804, 17043, 19423, 19424):
            super().sub_skill(skill)


class 新冥鼓无视防御(PhysicalShieldGainRecipe):
    value = -512

    def add_skill(self, skill: Skill):
        if skill.skill_id in (16758, 16759, 16760, 16382, 20991):
            super().add_skill(skill)

    def add_skills(self, skills: Dict[int, Skill]):
        skills[32823].physical_shield_gain = [self.value, 0, 0, self.value]
        skills[38537].physical_shield_gain = self.value
        return super().add_skills(skills)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (16758, 16759, 16760, 16382, 20991):
            super().sub_skill(skill)

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[32823].physical_shield_gain = 0
        skills[38537].physical_shield_gain = 0
        super().sub_skills(skills)


class 绝期_闹须弥增加持续伤害(ChannelIntervalRecipe):
    value = 1.7


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        SkillRecipe: {
            4127: dict(clone_id=16629), 4128: dict(clone_id=16629), 4129: dict(clone_id=16629),
            4143: {}, 4144: {}, 4145: {},
            4151: {}, 4152: {}, 4153: {},
            4159: {}, 4160: {}, 4161: {},
            4167: {}, 4168: {},
            4175: {}, 4176: {}, 4177: {},
            4183: {}, 4184: {}, 4185: {},
            4374: {}, 4375: {}, 4376: {},
            **{recipe_id: {} for recipe_id in range(2943, 2948 + 1)},
            3251: {}, 2509: {}, 2474: {}, **{recipe_id: {} for recipe_id in range(4257, 4264 + 1)},
            4290: {}, 4291: {}, 4294: {}, 4295: {}
        },
        CriticalStrikeRecipe_200: {
            4124: dict(clone_id=16629),
            4140: {},
            4148: {},
            4156: {},
            4164: {},
            4172: {},
            4180: {},
            4371: {},
        },
        CriticalStrikeRecipe_300: {
            4125: dict(clone_id=16629),
            4141: {},
            4149: {},
            4157: {},
            4165: {},
            4173: {},
            4181: {},
            4372: {}
        },
        CriticalStrikeRecipe_400: {
            4126: dict(clone_id=16629),
            4142: {},
            4150: {},
            4158: {},
            4166: {},
            4174: {},
            4182: {},
            4373: {}
        },
        CriticalStrikeRecipe_500: {
            4296: {}, 4297: {}
        },
        上将军印无视外防: {
            4298: {}
        },
        新冥鼓无视防御: {
            2510: {}, 2511: {}
        },
        绝期_闹须弥增加持续伤害: {
            4319: {}, 2833: {}
        }
    },
    1: {
        SkillRecipe: {
            17374: {}
        },
        CriticalStrikeRecipe_306: {
            17375: {}
        }
    }
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {
        "雷走风切": {
            "增加伤害5%": 4129,
            "增加伤害4%": 4128,
            "增加会心4%": 4126,
            "增加伤害3%": 4127,
            "增加会心3%": 4125,
            "增加会心2%": 4124,
        },
        "项王击鼎": {
            "增加伤害5%": 4145,
            "增加伤害4%": 4144,
            "增加会心4%": 4142,
            "增加伤害3%": 4143,
            "增加会心3%": 4141,
            "增加会心2%": 4140,
        },
        "破釜沉舟": {
            "增加伤害5%": 4153,
            "增加伤害4%": 4152,
            "增加会心4%": 4150,
            "增加伤害3%": 4151,
            "增加会心3%": 4149,
            "增加会心2%": 4148,
        },
        "碎江天": {
            "增加伤害5%": 4161,
            "增加伤害4%": 4160,
            "增加会心4%": 4158,
            "增加伤害3%": 4159,
            "增加会心3%": 4157,
            "增加会心2%": 4156,
        },
        "刀啸风吟": {
            "增加伤害5%": 4168,
            "增加伤害4%": 4167,
            "增加会心4%": 4166,
            "增加会心3%": 4165,
            "增加会心2%": 4164,
        },
        "醉斩白蛇": {
            "增加伤害5%": 4177,
            "增加伤害4%": 4176,
            "增加会心4%": 4174,
            "增加伤害3%": 4175,
            "增加会心3%": 4173,
            "增加会心2%": 4172,
        },
        "擒龙六斩": {
            "增加伤害5%": 4185,
            "增加伤害4%": 4184,
            "增加会心4%": 4182,
            "增加伤害3%": 4183,
            "增加会心3%": 4181,
            "增加会心2%": 4180,
        },
        "上将军印": {
            "增加伤害4%": 4376,
            "增加会心4%": 4373,
            "增加伤害3%": 4375,
            "增加会心3%": 4372,
            "增加会心2%": 4371,
            "增加伤害2%": 4374,
        }
    }
}
