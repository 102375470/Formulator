from general.recipes import *


class 新套装加钟林10(ChannelIntervalRecipe):
    value = 1.15


RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    SkillRecipe: {
        492: {}, 493: {},
        1677: {}, 1678: {}, 1679: {},
        4907: {}, 4908: {}, 4909: {},
        # 奇穴
        4661: {},
        # 装备
        1546: {}, 1516: {}, 1517: {}
    },
    CriticalStrikeRecipe_200: {
        490: {},
        4904: {}
    },
    CriticalStrikeRecipe_300: {
        491: {},
        4905: {}
    },
    CriticalStrikeRecipe_400: {
        4906: {}
    },
    CriticalStrikeRecipe_500: {
        1131: {}, 1979: {}
    },
    新套装加钟林10: {
        (817, 1): {}
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
    "阳明指": {
        "增加伤害4%": 493,
        "增加伤害3%": 492,
        "增加会心3%": 491,
        "增加会心2%": 490,
    },
    "快雪时晴": {
        "增加伤害5%": 1679,
        "增加伤害4%": 1678,
        "增加伤害3%": 1677
    },
    "芙蓉并蒂": {
        "增加伤害5%": 4909,
        "增加伤害4%": 4908,
        "增加会心4%": 4906,
        "增加伤害3%": 4907,
        "增加会心3%": 4905,
        "增加会心2%": 4904
    }
}
