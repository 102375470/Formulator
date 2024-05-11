from typing import Dict

from base.attribute import Attribute
from base.gain import Gain
from base.skill import Skill


class 封侯(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[18207].skill_damage_addition += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[18207].skill_damage_addition -= 102


class 扬戈(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[18207].skill_critical_strike += 1000
        skills[18207].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[18207].skill_critical_strike -= 1000
        skills[18207].skill_critical_power -= 102


class 神勇(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        for skill_id in (18773, 15002):
            skills[skill_id].skill_critical_strike += 1000
            skills[skill_id].skill_critical_power += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        for skill_id in (18773, 15002):
            skills[skill_id].skill_critical_strike -= 1000
            skills[skill_id].skill_critical_power -= 102


class 风虎(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[18207].skill_damage_addition += 205
        skills[18603].skill_damage_addition += 102
        for skill_id in [18773, 15002]:
            skills[skill_id].skill_damage_addition += 256
        for skill_id in [702, 24898, 6526]:
            skills[skill_id].skill_damage_addition += 102

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[18207].skill_damage_addition -= 205
        skills[18603].skill_damage_addition -= 102
        for skill_id in [18773, 15002]:
            skills[skill_id].skill_damage_addition -= 256
        for skill_id in [702, 24898, 6526]:
            skills[skill_id].skill_damage_addition -= 102


class 骁勇(Gain):
    def add_skills(self, skills: Dict[int, Skill]):
        skills[3442].attack_power_cof_gain *= 1.12

    def sub_skills(self, skills: Dict[int, Skill]):
        skills[3442].attack_power_cof_gain /= 1.12


TALENT_GAINS: Dict[int, Gain] = {
    18487: Gain("百折"),
    5656: 封侯("封侯"),
    5657: 扬戈("扬戈"),
    5660: 神勇("神勇"),
    5659: Gain("大漠"),
    18602: 骁勇("骁勇"),
    24896: Gain("龙驭"),
    14824: Gain("驰骋"),
    6511: Gain("牧云"),
    5666: 风虎("风虎"),
    6781: Gain("战心"),
    6524: Gain("破楼兰"),
    5678: Gain("夜征"),
    15001: Gain("龙血"),
    6517: Gain("虎贲")
}

TALENTS = [
    [18487, 5656, 5657],
    [5660],
    [5659, 18602],
    [24896],
    [14824],
    [6511],
    [5666],
    [6781],
    [6524],
    [5678],
    [15001],
    [6517],
]
TALENT_DECODER = {talent_id: talent.gain_name for talent_id, talent in TALENT_GAINS.items()}
TALENT_ENCODER = {v: k for k, v in TALENT_DECODER.items()}
