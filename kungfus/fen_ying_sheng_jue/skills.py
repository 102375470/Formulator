from typing import Dict

from base.skill import Skill


class 诛邪镇魔(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[25759].get(1):
            parser.clear_buff(25759)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_buff(25759, 1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


class 净世破魔击(Skill):
    def record(self, actual_critical_strike, actual_damage, parser):
        if parser.current_buff_stacks[70891].get(1):
            parser.refresh_target_buff(70188, 15)
            super().record(actual_critical_strike, actual_damage, parser)
            parser.refresh_target_buff(70188, 15, -1)
        else:
            super().record(actual_critical_strike, actual_damage, parser)


SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            4326: dict(channel_interval=16), 32816: {}, 19055: {}, 13468: {}, 3963: {}, 4035: {}, 4036: {}, 4476: {},
            4480: {}, 4482: {}, 18280: {}, 18281: {}, 26708: {}, 26709: {}, 35056: {}, 35057: {}, 34985: {}, 34348: {},
            34349: {}, 34362: {}, 34363: {}, 34359: {}, 34361: {}, 37336: {}, 25777: {}, 35065: {}, 14701: {},
            18631: dict(post_buffs={-12575: {1: 1}}),
            **{skill_id: {} for skill_id in range(4483, 4490 + 1)},
            13359: dict(bind_dots={4202: 1}),
            **{skill_id: dict(bind_dots={25725: 1}) for skill_id in (34373, 35038)},
            **{skill_id: dict(bind_dots={25726: 1}) for skill_id in (34374, 35039)}
        },
        诛邪镇魔: {
            26916: {}
        }
    },
    1: {
        Skill: {
            100644: {}, 100816: {}, 100720: {}, 100738: {}, 100721: {}, 101862: {},
            100718: dict(damage_addition_add=358),
            **{
                skill_id: dict(pre_target_buffs={70188: {50: 1}}, post_target_buffs={70188: {50: -1}})
                for skill_id in (100620, 100623, 100624)
            }
        },
        净世破魔击: {
            100649: {}, 100650: {}
        }
    }
}
