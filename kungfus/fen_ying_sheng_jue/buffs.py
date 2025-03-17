from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            # 奇穴
            4754: {}, 6277: {}, -12575: dict(buff_name="用晦而明", activate=False, interval=8),
            25759: dict(buff_name="明光·日"), 25758: dict(buff_name="明光·月")
        },
    },
    1: {
        Buff: {
            70891: {}
        }
    }
}
