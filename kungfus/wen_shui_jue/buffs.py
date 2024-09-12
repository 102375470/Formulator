from typing import Dict

from base.buff import Buff, CustomBuff

BUFFS: Dict[int, Dict[type, Dict[int, dict]]] = {
    0: {
        Buff: {
            1728: {}, 22913: {}, 12317: {}, 9714: {}, 26047: {}, 9903: {}, 26207: {}, 18008: {},
            21640: dict(buff_name="层云"),
        },
        CustomBuff: {-1: dict(buff_name="重剑", attributes=dict(weapon_damage_base=0))}
    }
}
