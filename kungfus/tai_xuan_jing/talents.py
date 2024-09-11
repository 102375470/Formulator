from typing import Dict, List

from base.gain import Gain

TALENTS: Dict[int, List[Dict[int, Gain]]] = {
    0: [
        {
            24936: Gain("水盈"),
            24925: Gain("正夏", recipes=[(5166, 1)]),
            24930: Gain("明心", recipes=[(5167, 1)])
        },
        {
            24932: Gain("天网"),
            24934: Gain("望旗", recipes=[(5170, 1)])
        },
        {
            25034: Gain("顺祝")
        },
        {
            32791: Gain("列宿游"),
            24994: Gain("龙回首"),
            25071: Gain("枭神")
        },
        {
            24983: Gain("重山", recipes=[(5179, 1), (5180, 1), (5181, 1)]),
            25025: Gain("地遁")
        },
        {
            25072: Gain("鬼遁"),
            25137: Gain("堪卜")
        },
        {
            25022: Gain("祝祷"),
            25368: Gain("亘天"),
            37456: Gain("追叙")
        },
        {
            25378: Gain("连断"),
            25066: Gain("神元", attributes=dict(spunk_gain=102))
        },
        {
            25085: Gain("荧入白")
        },
        {
            25379: Gain("征凶")
        },
        {
            25173: Gain("灵器")
        },
        {
            37505: Gain("镇星入舆")
        }
    ],
    1: []
}
