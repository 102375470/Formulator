from base.buff import Buff
from general.buffs import GENERAL_BUFFS


BUFFS = {
    11378: {
        "buff_name": "朔气",
        "gain_attributes": {
            "physical_critical_strike_gain": 400,
            "physical_critical_power_gain": 41
        }
    },
    18384: {
        "buff_name": "含风",
        "gain_attributes": {
            "physical_critical_strike_gain": 1000,
            "physical_critical_power_gain": 102
        }
    },
    23066: {
        "buff_name": "含风",
        "gain_skills": {
            16787: {
                "skill_damage_addition": 102,
            },
            16610: {
                "skill_damage_addition": 102,
            }
        }
    },
    14972: {
        "buff_name": "爆体",
        "gain_attributes": {
            "all_damage_addition": 205
        }
    }
}

for buff_id, detail in BUFFS.items():
    BUFFS[buff_id] = Buff(buff_id, detail.pop("buff_name"))
    for attr, value in detail.items():
        setattr(BUFFS[buff_id], attr, value)

for buff_id, buff in GENERAL_BUFFS.items():
    BUFFS[buff_id] = buff
