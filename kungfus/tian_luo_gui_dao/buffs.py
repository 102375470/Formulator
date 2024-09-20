from typing import Dict

from base.buff import Buff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            3254: {}, 3316: {}, 6105: {}, 8210: {}, 9981: {}, 27457: {}, 16234: {}, 16235: {}, 16236: {}, 6112: {},
            3426: {},
            10005: dict(stackable=False),
            13165: dict(buff_name="雷甲三铉"),
            27405: dict(buff_name="雷甲三铉"),
            23081: dict(buff_name="擘两分星"),
            23082: dict(buff_name="擘两分星"),
            -24668: dict(buff_name="杀机断魂", activate=False, max_stack=20)
        }
    }
}
