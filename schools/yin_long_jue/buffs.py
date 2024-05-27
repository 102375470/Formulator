from typing import Dict, Union

from base.buff import Buff
from general.buffs import GENERAL_BUFFS

BUFFS: Dict[int, Union[Buff, dict]] = {
    16025: {
        "buff_name": "雷引",
        "activate": False,
        "gain_attributes": {
            "physical_critical_strike_rate": 400,
            "physical_critical_power_rate": 41
        }
    },
    16596: {
        "buff_name": "崔嵬鬼步",
        "gain_attributes": {
            "physical_attack_power_gain": 154,
            "physical_critical_strike_rate": 1500,
            "physical_critical_power_rate": 150
        }
    },
    15893: {
        "buff_name": "忘断",
        "gain_attributes": {
            "physical_attack_power_gain": 256
        }
    },
    15927: {
        "buff_name": "百节",
        "frame_shift": -2,
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 102
            } for skill_id in
            [22610, 22611, 22612, 36269, 36270] + [22604, 22605, 36267, 36268] + [22490, 22554, 36265, 36266]
        }
    },
    15928: {
        "buff_name": "百节",
        "frame_shift": -2,
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 205
            } for skill_id in
            [22610, 22611, 22612, 36269, 36270] + [22604, 22605, 36267, 36268] + [22490, 22554, 36265, 36266]
        }
    },
    15929: {
        "buff_name": "百节",
        "frame_shift": -2,
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": 307
            } for skill_id in
            [22610, 22611, 22612, 36269, 36270] + [22604, 22605, 36267, 36268] + [22490, 22554, 36265, 36266]
        }
    },
    15832: {
        "buff_name": "星旗",
        "gain_skills": {
            skill_id: {
                "skill_damage_addition": [154, 307]
            } for skill_id in (22170, 22550, 22551, 22298)
        }
    },
    15932: {
        "buff_name": "徵逐",
        "gain_attributes": {
            "all_shield_ignore": 512
        }
    }
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id)
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    if buff_id not in BUFFS:
        BUFFS[buff_id] = buff
