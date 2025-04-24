from typing import Dict

from base.buff import Buff

BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        20938: {}, 23107: {}, 6363: {}, 6214: {}, 24350: {}, 29354: {}, 24742: {}, 8504: {}, 10031: {},
        23543: {}, 11456: {}, 20877: {}, 29294: {}, 20854: {},
        16911: dict(buff_name="弄梅"),
        23573: dict(buff_name="泠风解怀"),
        4246: dict(buff_name=["朝圣言", "圣浴明心"]),
        -673: {}, -362: {}, -661: {}, -3465: {}, -566: {}, -378: {}, -375: {}, -4058: {}, -8248: {},
        -12717: dict(buff_name="劲风"),
        # 坦克
        -17885: dict(buff_name="宿敌增益"), -29938: dict(buff_name="坦克增益")
    }
}
