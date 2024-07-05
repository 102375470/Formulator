from dataclasses import dataclass
from typing import Dict, List, Union

from base.attribute import Attribute
from base.skill import Skill

ATTR_DICT = Dict[str, Union[List[int], int]]


class BaseBuff:
    DOT_SNAPSHOT_ATTRS = [
        "attack_power", "critical_strike", "critical_power", "surplus", "strain", "damage_addition", "pve_addition"
    ]
    PET_SNAPSHOT_ATTRS = [
        "attack_power", "critical_power", "overcome", "surplus", "strain", "damage_addition", "pve_addition"
    ]

    buff_level: int = 0
    buff_stack: int = 1
    _buff_name: List[str] = None

    _max_stack: List[int] = None
    interval: int = 0

    @property
    def buff_name(self):
        if not self._buff_name:
            return ""
        if self.buff_level > len(self._buff_name):
            return self._buff_name[-1]
        else:
            return self._buff_name[self.buff_level - 1]

    @buff_name.setter
    def buff_name(self, buff_name):
        if isinstance(buff_name, list):
            self._buff_name = buff_name
        else:
            self._buff_name = [buff_name]

    @property
    def max_stack(self):
        if not self._max_stack:
            return 1
        if self.buff_level > len(self._max_stack):
            return self._max_stack[-1]
        else:
            return self._max_stack[self.buff_level - 1]

    @max_stack.setter
    def max_stack(self, max_stack):
        if isinstance(max_stack, list):
            self._max_stack = max_stack
        else:
            self._max_stack = [max_stack]


@dataclass
class Buff(BaseBuff):
    buff_id: int

    frame_shift: int = 0
    unique: bool = True
    activate: bool = True

    gains: list = None
    attributes: ATTR_DICT = None

    begin_effects: list = None
    begin_buffs: dict = None
    begin_target_buffs: dict = None
    end_effects: list = None
    end_buffs: dict = None
    end_target_buffs: dict = None

    def __post_init__(self):
        if self.gains is None:
            self.gains = []
        if self.attributes is None:
            self.attributes = {}
        if not self.begin_buffs:
            self.begin_buffs = {}
        if not self.begin_target_buffs:
            self.begin_target_buffs = {}
        if not self.begin_effects:
            self.begin_effects = []
        if not self.end_buffs:
            self.end_buffs = {}
        if not self.end_target_buffs:
            self.end_target_buffs = {}
        if not self.end_effects:
            self.end_effects = []

    @property
    def display_name(self):
        return f"{self.buff_name}#{self.buff_id}-{self.buff_level}-{self.buff_stack}"

    def attribute_value(self, values):
        if isinstance(values, list):
            return values[self.buff_level - 1] * self.buff_stack
        else:
            return values * self.buff_stack

    def gain_value(self, values):
        if isinstance(values, list):
            return values[self.buff_level - 1]
        else:
            return values

    def begin(self, parser):
        for (buff_id, buff_level), buff_stack in self.begin_buffs.items():
            buff_level = buff_level if buff_level else self.buff_level
            parser.refresh_buff(buff_id, buff_level, buff_stack)
        for (buff_id, buff_level), buff_stack in self.begin_target_buffs.items():
            buff_level = buff_level if buff_level else self.buff_level
            parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.begin_effects:
            effect(parser)

    def end(self, parser):
        for (buff_id, buff_level), buff_stack in self.end_buffs.items():
            buff_level = buff_level if buff_level else self.buff_level
            parser.refresh_buff(buff_id, buff_level, buff_stack)
        for (buff_id, buff_level), buff_stack in self.end_target_buffs.items():
            buff_level = buff_level if buff_level else self.buff_level
            parser.refresh_target_buff(buff_id, buff_level, buff_stack)
        for effect in self.end_effects:
            effect(parser)

    def add_all(self, attribute: Attribute, skill: Skill):
        return_tag = False
        for attr, values in self.attributes.items():
            value = self.attribute_value(values)
            if not value:
                continue
            setattr(attribute, attr, getattr(attribute, attr) + value)
            return_tag = True
        for values in self.gains:
            if self.gain_value(values).add(attribute, {skill.skill_id: skill}, {self.buff_id: self}):
                return_tag = True

        return return_tag

    def add_dot(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        return_tag = False
        for attr, values in self.attributes.items():
            value = self.attribute_value(values)
            if not value:
                continue
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) + value)
                return_tag = True
            if not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) + value)
                return_tag = True

        if snapshot:
            for values in self.gains:
                if self.gain_value(values).add(attribute, {skill.skill_id: skill}, {self.buff_id: self}):
                    return_tag = True

        return return_tag

    def add_pet(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        return_tag = False
        for attr, values in self.attributes.items():
            value = self.attribute_value(values)
            if not value:
                continue
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.PET_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) + value)
                return_tag = True
            if not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.PET_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) + value)
                return_tag = True
        if snapshot:
            for values in self.gains:
                if self.gain_value(values).add(attribute, {skill.skill_id: skill}, {self.buff_id: self}):
                    return_tag = True

        return return_tag

    def sub_all(self, attribute: Attribute, skill: Skill):
        for attr, values in self.attributes.items():
            value = self.attribute_value(values)
            if not value:
                continue
            setattr(attribute, attr, getattr(attribute, attr) - value)
        for values in self.gains:
            self.gain_value(values).sub(attribute, {skill.skill_id: skill}, {self.buff_id: self})

    def sub_dot(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        for attr, values in self.attributes.items():
            value = self.attribute_value(values)
            if not value:
                continue
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - value)
            if not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.DOT_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - value)
        if snapshot:
            for values in self.gains:
                self.gain_value(values).sub(attribute, {skill.skill_id: skill}, {self.buff_id: self})

    def sub_pet(self, attribute: Attribute, skill: Skill, snapshot: bool = True):
        for attr, values in self.attributes.items():
            value = self.attribute_value(values)
            if not value:
                continue
            if snapshot and any(snapshot_attr in attr for snapshot_attr in self.PET_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - value)
            if not snapshot and all(snapshot_attr not in attr for snapshot_attr in self.PET_SNAPSHOT_ATTRS):
                setattr(attribute, attr, getattr(attribute, attr) - value)
        if snapshot:
            for values in self.gains:
                self.gain_value(values).sub(attribute, {skill.skill_id: skill}, {self.buff_id: self})


class TargetBuff(Buff):
    def add_all(self, attribute: Attribute, skill: Skill):
        return super().add_all(attribute.target, skill)

    def sub_all(self, attribute: Attribute, skill: Skill):
        super().sub_all(attribute.target, skill)


class CustomBuff(Buff):
    pass
