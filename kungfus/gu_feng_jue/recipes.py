from general.recipes import *


class 纷绞势双会提高秘籍(PhysicalCriticalRecipe):
    value = (1000, 102)


class 沧浪三叠双会提高秘籍(PhysicalCriticalRecipe):
    values = [(1000, 102), (2000, 205), (3000, 307)]

    def add_skill(self, skill: Skill):
        if skill.skill_id in (32216, 32359, 32602):
            self.value = self.values[0]
            super().add_skill(skill)
        elif skill.skill_id in (32217, 32360, 32603):
            self.value = self.values[1]
            super().add_skill(skill)
        elif skill.skill_id in (32218, 32361, 32604):
            self.value = self.values[2]
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (32216, 32359, 32602):
            self.value = self.values[0]
            super().sub_skill(skill)
        elif skill.skill_id in (32217, 32360, 32603):
            self.value = self.values[1]
            super().sub_skill(skill)
        elif skill.skill_id in (32218, 32361, 32604):
            self.value = self.values[2]
            super().sub_skill(skill)


RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    DotRecipe: {
        -161: {}, -162: {}
    },
    SkillRecipe: {
        3041: {}, 3042: {}, 3112: {},
        3045: {}, 3046: {},
        3049: {}, 3050: {},
        3053: {}, 3054: {}, 3128: {},
        3057: {}, 3058: {},
        3061: {}, 3062: {},
        3065: {}, 3066: {}, 3142: {},
        3133: {}, 3134: {},
        3137: {}, 3138: {},
        # 奇穴
        5584: {}, 5585: {}, 5586: {},
        # 装备
        3188: {}, 3186: {}, 3187: {}, 5754: {}
    },
    CriticalStrikeRecipe_200: {
        3111: {},
        3217: {},
        3139: {},
        3141: {}
    },
    CriticalStrikeRecipe_300: {
        2992: {},
        3043: {},
        3047: {},
        3051: {},
        3055: {},
        3059: {},
        3063: {},
        3140: {}
    },
    CriticalStrikeRecipe_400: {
        3040: {},
        3044: {},
        3048: {},
        3052: {},
        3056: {},
        3060: {},
        3064: {}
    },
    CriticalStrikeRecipe_500: {
        3185: {}
    },
    纷绞势双会提高秘籍: {
        3011: {}
    },
    沧浪三叠双会提高秘籍: {
        3023: {}
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
    "行云式": {
        "增加伤害5%": 3042,
        "增加伤害4%": 3041,
        "增加会心4%": 3040,
        "增加伤害3%": 3112,
        "增加会心3%": 2992,
        "增加会心2%": 3111,
    },
    "停云势": {
        "增加伤害5%": 3046,
        "增加伤害4%": 3045,
        "增加会心4%": 3044,
        "增加会心3%": 3043,
    },
    "断云势": {
        "增加伤害5%": 3050,
        "增加伤害4%": 3049,
        "增加会心4%": 3048,
        "增加会心3%": 3047,
    },
    "沧浪三叠": {
        "增加伤害5%": 3054,
        "增加伤害4%": 3053,
        "增加伤害3%": 3128,
        "增加会心4%": 3052,
        "增加会心3%": 3051,
        "增加会心2%": 3127,
    },
    "横云断浪": {
        "增加伤害5%": 3058,
        "增加伤害4%": 3057,
        "增加会心4%": 3056,
        "增加会心3%": 3055,
    },
    "孤锋破浪": {
        "增加伤害5%": 3062,
        "增加伤害4%": 3061,
        "增加会心4%": 3060,
        "增加会心3%": 3059,
    },
    "留客雨": {
        "增加伤害5%": 3066,
        "增加伤害4%": 3065,
        "增加伤害3%": 3142,
        "增加会心4%": 3064,
        "增加会心3%": 3063,
        "增加会心2%": 3141,
    },
    "触石雨": {
        "增加伤害4%": 3134,
        "增加伤害3%": 3133,
    },
    "决云势": {
        "增加伤害4%": 3138,
        "增加伤害3%": 3137,
        "增加会心3%": 3140,
        "增加会心2%": 3139,
    }
}
