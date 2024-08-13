from typing import Dict

from base.buff import Buff
from base.recipe import DamageAdditionRecipe
from general.buffs import GENERAL_BUFFS

SCHOOL_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        11378: {}, 24553: {}, 24209: {},
        24179: dict(buff_name="雨积",
                    gains=[DamageAdditionRecipe(154, skill_id, skill_id) for skill_id in (32132, 32133)]),
        24557: dict(gains=[DamageAdditionRecipe(82, skill_id, skill_id) for skill_id in (32145, 32144, 32601)]),
        24180: dict(buff_name="镇机", gains=[
            [DamageAdditionRecipe(value, 32135, 32135) for value in (123, 246, 369, 492, 614, 737, 1075, 1229)]
        ])
    }
}
MOBILE_BUFFS: Dict[type, Dict[int, dict]] = {
    Buff: {
        71297: {}
    }
}
BUFFS: Dict[int, Buff] = {**GENERAL_BUFFS}
for buff_class, buffs in SCHOOL_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        buff.set_asset()
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
for buff_class, buffs in MOBILE_BUFFS.items():
    for buff_id, attrs in buffs.items():
        buff = buff_class(buff_id)
        buff.set_asset()
        for attr, value in attrs.items():
            setattr(buff, attr, value)
        BUFFS[buff_id] = buff
