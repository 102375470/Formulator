from typing import Dict

from base.skill import Skill

SKILLS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Skill: {
            15: dict(channel_interval=21), 506: {}, 2716: {}, 6234: {}, 6554: {}, 6559: {}, 23936: {}, 24999: {},
            25769: {}, 30524: {}, 30532: {}, 32957: {}, 34612: {}, 34642: {}, 35058: {}, 37317: {}, 34704: {},
            37318: {},  37319: {}, 37320: {}, 36554: {}, 32889: {}, 34611: {},
            **{skill_id: dict(bind_dots={2920: 1}) for skill_id in (6207, 18716)},
            25757: dict(bind_dots={18512: 1}),
            3889: dict(consume_dots={2920: 0})
        }
    },
    1: {
        Skill: {
            100388: {}, 101635: {}, 101655: {}, 101649: {}, 101610: {}, 101612: {}, 101609: {}, 100444: {}, 100564: {},
            100414: {}, 100418: {},
            100402: dict(bind_dots={70030: 1}),
            101553: dict(consume_dots={70030: 1}),
            101607: dict(consume_dots={70030: 0})
        }
    }
}
