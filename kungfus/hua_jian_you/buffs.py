from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            1487: {}, 11809: {}, 28116: {}, -24599: {},
            -9722: dict(interval=320),
            14636: dict(buff_name="乱洒"),
            -12588: dict(buff_name="清流", activate=False),
        }
    }
}
