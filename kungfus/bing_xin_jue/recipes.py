from general.recipes import *


class 阴性会心提高10(LunarCriticalRecipe):
    values = [(1500, 154), (1000, 102)]

    def add_skill(self, skill: Skill):
        if skill.skill_id in (569, 2976, 2977, 6209, 21275, 22736, 22737):
            self.value = self.values[0]
        else:
            self.value = self.values[1]
        super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (569, 2976, 2977, 6209, 21275, 22736, 22737):
            self.value = self.values[0]
        else:
            self.value = self.values[1]
        super().sub_skill(skill)


class 剑破会心20(LunarCriticalRecipe):
    value = (1000, 102)


RECIPES: Dict[int, Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]]] = {
    0: {
        SkillRecipe: {
            145: {}, 146: {},
            160: {}, 161: {},
            1637: {}, 1638: {}, 1639: {},
            3246: {},
            2893: {}, 1488: {}, 4478: {}, 5634: {},
            1547: {}, 1524: {}, 1525: {}
        },
        CriticalStrikeRecipe_200: {
            143: {}, 155: {}
        },
        CriticalStrikeRecipe_300: {
            144: {}, 156: {}
        },
        CriticalStrikeRecipe_500: {
            1137: {}, 1977: {}
        },
        阴性会心提高10: {
            1246: {}
        },
        剑破会心20: {
            2014: {}, 2015: {}, 2016: {}
        }
    },
    1: {
        SkillRecipe: {
            17380: {}
        },
        CriticalStrikeRecipe_306: {
            17381: {}
        }
    }
}
RECIPE_CHOICES: Dict[int, Dict[str, Dict[str, int]]] = {
    0: {
        "剑气长江": {
            "增加伤害6%": 146,
            "增加伤害4%": 145,
            "增加会心3%": 144,
            "增加会心2%": 143,
        },
        "江海凝光": {
            "增加伤害15%·1": 160,
            "增加伤害15%·2": 161,
            "增加会心3%": 156,
            "增加会心2%": 155,
        },
        "玳弦急曲": {
            "增加伤害5%": 1639,
            "增加伤害4%": 1638,
            "增加伤害3%": 1637,
        }
    }
}
