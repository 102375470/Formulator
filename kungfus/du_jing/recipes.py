from general.recipes import *


class 蛇影加伤害1(ChannelIntervalRecipe):
    value = 1.04


class 蛇影加伤害2(ChannelIntervalRecipe):
    value = 1.05


class 蛇影加伤害10(ChannelIntervalRecipe):
    value = 1.1


class 百足加伤害1(ChannelIntervalRecipe):
    value = 1.05


class 百足加伤害2(ChannelIntervalRecipe):
    value = 1.1


class 蝎心加伤害2(ChannelIntervalRecipe):
    value = 1.2

    def add_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            super().sub_skill(skill)


class 蝎心加伤害3(ChannelIntervalRecipe):
    value = 1.03

    def add_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            super().sub_skill(skill)


class 蝎心加伤害4(ChannelIntervalRecipe):
    value = 1.04

    def add_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            super().sub_skill(skill)


class 蝎心加伤害5(ChannelIntervalRecipe):
    value = 1.05

    def add_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id == 13476:
            super().sub_skill(skill)


class 蝎心加会心(PoisonCriticalRecipe):
    value = (1000, 100)


class 蛇影提高伤害(ChannelIntervalRecipe):
    value = 1.25


class 黯影蛇影提高伤害(ChannelIntervalRecipe):
    value = 1.25


class 百足提高伤害(ChannelIntervalRecipe):
    value = 1.25


class 蟾啸提高伤害(ChannelIntervalRecipe):
    value = 1.25


class 蝎心提高伤害(ChannelIntervalRecipe):
    value = 1.25


class 橙武提高伤害(ChannelIntervalRecipe):
    value = 1.25


class 新忘情增伤(ChannelIntervalRecipe):
    value = 1.6

    def add_skill(self, skill: Skill):
        if skill.skill_id in (6237, 21303, 6236, 13473):
            super().add_skill(skill)

    def sub_skill(self, skill: Skill):
        if skill.skill_id in (6237, 21303, 6236, 13473):
            super().sub_skill(skill)


RECIPES: Dict[type(Recipe), Dict[Union[int, Tuple[int, int]], dict]] = {
    DotRecipe: {
        -134: dict(clone_id=25917)
    },
    SkillRecipe: {
        746: {}, 747: {}, 748: {},
        # 奇穴
        (677, 2): {}, **{recipe_id: {} for recipe_id in list(range(3228, 3233 + 1)) + [3254, 3255, 3297, 3298, 3299]},
        5608: {}, **{recipe_id: {} for recipe_id in range(2513, 2516 + 1)},
        # 装备
        1529: {},
    },
    CriticalStrikeRecipe_200: {
        762: {},
        794: {},
    },
    CriticalStrikeRecipe_300: {
        763: {},
        795: {}
    },
    CriticalStrikeRecipe_400: {
        764: {}
    },
    CriticalStrikeRecipe_500: {
        1143: {}
    },
    蛇影加伤害1: {
        767: {}
    },
    蛇影加伤害2: {
        768: {}
    },
    蛇影加伤害10: {
        4678: {}
    },
    百足加伤害1: {
        774: {}
    },
    百足加伤害2: {
        773: {}, 775: {}
    },
    蝎心加伤害2: {
        (818, 7): {}
    },
    蝎心加伤害3: {
        796: {}
    },
    蝎心加伤害4: {
        797: {}
    },
    蝎心加伤害5: {
        1528: {}
    },
    蝎心加会心: {
        1265: {}, 2427: {}
    },
    蛇影提高伤害: {
        1269: {}
    },
    黯影蛇影提高伤害: {
        3263: {}
    },
    百足提高伤害: {
        1270: {}, 4550: {}, 5538: {}
    },
    蟾啸提高伤害: {
        1271: {}
    },
    蝎心提高伤害: {
        1272: {}
    },
    橙武提高伤害: {
        2436: {}
    },
    新忘情增伤: {
        5891: {}, 5898: {}, 5901: {}
    }
}
RECIPE_CHOICES: Dict[str, Dict[str, int]] = {
    "灵蛊": {
        "增加伤害10%·1": 746,
        "增加伤害10%·2": 747,
        "增加伤害10%·3": 748,
    },
    "蛇影": {
        "增加伤害5%": 768,
        "增加伤害4%": 767,
        "增加会心4%": 764,
        "增加会心3%": 763,
        "增加会心2%": 762
    },
    "百足": {
        "增加伤害10%·1": 773,
        "增加伤害10%·2": 775,
        "增加伤害5%": 774
    },
    "蝎心": {
        "增加伤害4%": 797,
        "增加伤害3%": 796,
        "增加会心3%": 795,
        "增加会心2%": 794,
    }
}
