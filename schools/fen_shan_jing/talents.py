from typing import Dict

from base.gain import Gain
from base.skill import Skill


class 分野(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[13075].skill_critical_strike += 1500
        skills[13075].skill_critical_power += 200

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[13075].skill_critical_strike -= 1500
        skills[13075].skill_critical_power -= 200


TALENT_GAINS: Dict[int, Gain] = {
    13317: Gain("刀魂"),
    13090: Gain("绝返"),
    13087: 分野("分野"),
    21281: Gain("血魄"),
    22897: Gain("锋鸣"),
    37239: Gain("麾远"),
    34912: Gain("业火麟光"),
    13126: Gain("恋战"),
    36058: Gain("援戈"),
    36205: Gain("惊涌"),
    14838: Gain("蔑视"),
    30769: Gain("阵云结晦")
}

TALENTS = [
    [13317],
    [13090],
    [13087],
    [21281],
    [22897],
    [37239],
    [34912],
    [13126],
    [36058],
    [36205],
    [14838],
    [30769]
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
