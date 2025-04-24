from typing import Dict

from base.skill import Skill

SKILLS: Dict[type, Dict[int, dict]] = {
    Skill: {
        15: dict(channel_interval=21), 32957: {}, 34704: {}, 32889: {}, 34611: {}, 40289: {},
        # 猿公剑法
        40182: {}, 6234: {}, 30524: {}, 3889: dict(consume_dots={2920: 0}),
        **{skill_id: dict(bind_dots={2920: 1}) for skill_id in (6207, 18716)},
        # 西河剑器
        6559: {},
        # 剑器浑脱
        568: dict(post_buffs={10240: {1: 5}, 538: {4: 1}}),
        # 奇穴
        6554: {}, **{skill_id: {} for skill_id in range(37317, 37320 + 1)}, 23936: {}, 33140: {},
        30532: {}, 24999: {}, 34612: {}, 35058: {},
        # 装备
        25769: {}, 25757: dict(bind_dots={18512: 1}),
    }
}
