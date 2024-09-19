from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            18384: {}, 23066: {}, 19510: {}, 19244: {},
            29218: dict(buff_name="爆体"), 11221: dict(buff_name="化蛟"), 19499: dict(buff_name="砺锋")
        }
    },
    1: {
        Buff: {
            71047: {}, 70454: dict(interval=16)
        }
    }
}
