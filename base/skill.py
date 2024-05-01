from base.attribute import Attribute
from base.constant import *
from utils.damage import *

from typing import List, Union
from dataclasses import dataclass


@dataclass
class Skill:
    skill_id: int
    _skill_name: Union[List[str], str] = ""
    skill_level: int = 0
    skill_stack: int = 1

    activate: bool = True

    bind_skill: int = None
    bind_buff: int = None
    max_stack: int = 1
    tick: int = 1

    _damage_base: Union[List[int], int] = 0
    _damage_rand: Union[List[int], int] = 0

    _attack_power_cof: Union[List[float], float] = 0.
    _surplus_cof: Union[List[float], float] = 0.
    _weapon_damage_cof: Union[List[float], float] = 0.

    interval: int = 0

    damage_gain: float = 1.
    attack_power_cof_gain: float = 1.
    surplus_cof_gain: float = 1.
    weapon_damage_cof_gain: float = 1.

    skill_damage_addition: int = 0
    skill_pve_addition: int = 0
    _skill_shield_gain: Union[List[int], int] = 0
    skill_critical_strike: int = 0
    skill_critical_power: int = 0

    @property
    def display_name(self):
        return f"{self.skill_name}#{self.skill_id}-{self.skill_level}-{self.skill_stack}"

    @property
    def skill_name(self):
        if not isinstance(self._skill_name, list):
            return ""

        if self.skill_level > len(self._skill_name):
            return self._skill_name[-1]
        else:
            return self._skill_name[self.skill_level - 1]

    @skill_name.setter
    def skill_name(self, skill_name):
        if isinstance(skill_name, list):
            self._skill_name = skill_name
        else:
            self._skill_name = [skill_name]

    @property
    def damage_base(self):
        if not isinstance(self._damage_base, list):
            return 0

        if self.skill_level > len(self._damage_base):
            damage_base = self._damage_base[-1]
        else:
            damage_base = self._damage_base[self.skill_level - 1]
        return damage_base * self.damage_gain

    @damage_base.setter
    def damage_base(self, damage_base):
        if isinstance(damage_base, list):
            self._damage_base = damage_base
        else:
            self._damage_base = [damage_base]

    @property
    def damage_rand(self):
        if not isinstance(self._damage_rand, list):
            return 0

        if self.skill_level > len(self._damage_rand):
            damage_rand = self._damage_rand[-1]
        else:
            damage_rand = self._damage_rand[self.skill_level - 1]
        return damage_rand * self.damage_gain

    @damage_rand.setter
    def damage_rand(self, damage_rand):
        if isinstance(damage_rand, list):
            self._damage_rand = damage_rand
        else:
            self._damage_rand = [damage_rand]

    @property
    def attack_power_cof(self):
        if not isinstance(self._attack_power_cof, list):
            return 0

        if self.skill_level > len(self._attack_power_cof):
            attack_power_cof = self._attack_power_cof[-1]
        else:
            attack_power_cof = self._attack_power_cof[self.skill_level - 1]
        return attack_power_cof * self.attack_power_cof_gain

    @attack_power_cof.setter
    def attack_power_cof(self, attack_power_cof):
        if isinstance(attack_power_cof, list):
            self._attack_power_cof = attack_power_cof
        else:
            self._attack_power_cof = [attack_power_cof]

    @property
    def surplus_cof(self):
        if not isinstance(self._surplus_cof, list):
            return 0

        if self.skill_level > len(self._surplus_cof):
            surplus_cof = self._surplus_cof[-1]
        else:
            surplus_cof = self._surplus_cof[self.skill_level - 1]
        return SURPLUS_COF(surplus_cof * self.surplus_cof_gain)

    @surplus_cof.setter
    def surplus_cof(self, surplus_cof):
        if isinstance(surplus_cof, list):
            self._surplus_cof = surplus_cof
        else:
            self._surplus_cof = [surplus_cof]

    @property
    def weapon_damage_cof(self):
        if not isinstance(self._weapon_damage_cof, list):
            return 0

        if self.skill_level > len(self._weapon_damage_cof):
            weapon_damage_cof = self._weapon_damage_cof[-1]
        else:
            weapon_damage_cof = self._weapon_damage_cof[self.skill_level - 1]
        return WEAPON_DAMAGE_COF(weapon_damage_cof * self.weapon_damage_cof_gain)

    @weapon_damage_cof.setter
    def weapon_damage_cof(self, weapon_damage_cof):
        if isinstance(weapon_damage_cof, list):
            self._weapon_damage_cof = weapon_damage_cof
        else:
            self._weapon_damage_cof = [weapon_damage_cof]

    @property
    def skill_shield_gain(self):
        if not isinstance(self._skill_shield_gain, list):
            return 0

        if self.skill_level > len(self._skill_shield_gain):
            return self._skill_shield_gain[-1]
        else:
            return self._skill_shield_gain[self.skill_level - 1]

    @skill_shield_gain.setter
    def skill_shield_gain(self, skill_shield_gain):
        if isinstance(skill_shield_gain, list):
            self._skill_shield_gain = skill_shield_gain
        else:
            self._skill_shield_gain = [skill_shield_gain]

    def record(self, current_frame, player_id, skill_level, skill_stack, critical, parser):
        pass

    def __call__(self, attribute: Attribute):
        return 0


class BuffSkill(Skill):
    pass


class BuffConsumeSkill(Skill):
    pass


class DotSkill(Skill):
    def record(self, current_frame, player_id, skill_level, skill_stack, critical, parser):
        super().record(current_frame, player_id, skill_level, skill_stack, critical, parser)
        bind_skill = self.bind_skill
        if not parser.ticks[player_id][bind_skill]:
            parser.stacks[player_id][bind_skill] = 0
        parser.ticks[player_id][bind_skill] = self.tick
        parser.stacks[player_id][bind_skill] = min(parser.stacks[player_id][bind_skill] + 1, self.max_stack)
        parser.snapshot[player_id][bind_skill] = parser.status[player_id].copy()


class DotConsumeSkill(Skill):
    def record(self, current_frame, player_id, skill_level, skill_stack, critical, parser):
        super().record(current_frame, player_id, skill_level, skill_stack, critical, parser)
        bind_skill = self.bind_skill
        skill_tuple, status_tuple = parser.last_dot[player_id][bind_skill]
        skill_id, skill_level, skill_stack = skill_tuple
        parser.ticks[player_id][skill_id] += 1
        tick = min(parser.ticks[player_id][skill_id], self.tick)
        current_record = parser.records[player_id][-1]
        current_record[(skill_id, skill_level, skill_stack * tick)][status_tuple].append(
            current_record[skill_tuple][status_tuple].pop()
        )
        parser.ticks[player_id][skill_id] -= tick


class PureSkill(Skill):
    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, self.damage_rand,
            0, 0,
            0, 0, 0, 0
        )

        damage = level_reduction_result(damage, attribute.level_reduction)
        damage = vulnerable_result(damage, attribute.vulnerable)

        return damage, damage, damage, 0


class PhysicalSkill(Skill):
    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, self.damage_rand,
            self.attack_power_cof, attribute.physical_attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            self.surplus_cof, attribute.surplus
        ) * self.skill_stack

        damage = damage_addition_result(damage, attribute.physical_damage_addition + self.skill_damage_addition)
        damage = overcome_result(damage, attribute.physical_overcome,
                                 attribute.level_shield_base + attribute.physical_shield_base,
                                 attribute.physical_shield_gain + self.skill_shield_gain,
                                 attribute.physical_shield_ignore,
                                 attribute.shield_constant)

        critical_power_gain = attribute.physical_critical_power_gain + self.skill_critical_power
        critical_damage = critical_result(damage, attribute.base_physical_critical_power, critical_power_gain)

        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.base_strain, attribute.strain_gain)
        critical_damage = strain_result(critical_damage, attribute.base_strain, attribute.strain_gain)
        damage = pve_addition_result(damage, attribute.pve_addition + self.skill_pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, attribute.physical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.physical_vulnerable)
        critical_strike = min(1, attribute.physical_critical_strike + self.skill_critical_strike / DECIMAL_SCALE)

        expected_damage = critical_strike * critical_damage + (1 - critical_strike) * damage

        return damage, critical_damage, expected_damage, critical_strike


class MagicalSkill(Skill):
    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, self.damage_rand,
            self.attack_power_cof, attribute.magical_attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            self.surplus_cof, attribute.surplus
        ) * self.skill_stack

        damage = damage_addition_result(damage, attribute.magical_damage_addition + self.skill_damage_addition)
        damage = overcome_result(damage, attribute.magical_overcome,
                                 attribute.level_shield_base + attribute.magical_shield_base,
                                 attribute.magical_shield_gain + self.skill_shield_gain,
                                 attribute.magical_shield_ignore,
                                 attribute.shield_constant)

        critical_power_gain = attribute.magical_critical_power_gain + self.skill_critical_power
        critical_damage = critical_result(damage, attribute.base_magical_critical_power, critical_power_gain)

        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.base_strain, attribute.strain_gain)
        critical_damage = strain_result(critical_damage, attribute.base_strain, attribute.strain_gain)
        damage = pve_addition_result(damage, attribute.pve_addition + self.skill_pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, attribute.magical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.magical_vulnerable)
        critical_strike = min(1, attribute.magical_critical_strike + self.skill_critical_strike / DECIMAL_SCALE)

        expected_damage = critical_strike * critical_damage + (1 - critical_strike) * damage

        return damage, critical_damage, expected_damage, critical_strike


class MixingSkill(Skill):
    def __call__(self, attribute: Attribute):
        damage = init_result(
            self.damage_base, self.damage_rand,
            self.attack_power_cof, attribute.magical_attack_power,
            self.weapon_damage_cof, attribute.weapon_damage,
            self.surplus_cof, attribute.surplus
        ) * self.skill_stack

        damage = damage_addition_result(damage, attribute.magical_damage_addition + self.skill_damage_addition)
        damage = overcome_result(damage, attribute.magical_overcome,
                                 attribute.level_shield_base + attribute.magical_shield_base,
                                 attribute.magical_shield_gain + self.skill_shield_gain,
                                 attribute.magical_shield_ignore,
                                 attribute.shield_constant)

        critical_power_gain = attribute.physical_critical_power_gain + self.skill_critical_power
        critical_damage = critical_result(damage, attribute.base_physical_critical_power, critical_power_gain)

        damage = level_reduction_result(damage, attribute.level_reduction)
        critical_damage = level_reduction_result(critical_damage, attribute.level_reduction)
        damage = strain_result(damage, attribute.base_strain, attribute.strain_gain)
        critical_damage = strain_result(critical_damage, attribute.base_strain, attribute.strain_gain)
        damage = pve_addition_result(damage, attribute.pve_addition + self.skill_pve_addition)
        critical_damage = pve_addition_result(critical_damage, attribute.pve_addition + self.skill_pve_addition)
        damage = vulnerable_result(damage, attribute.magical_vulnerable)
        critical_damage = vulnerable_result(critical_damage, attribute.magical_vulnerable)
        critical_strike = min(1, attribute.physical_critical_strike + self.skill_critical_strike / DECIMAL_SCALE)

        expected_damage = critical_strike * critical_damage + (1 - critical_strike) * damage

        return damage, critical_damage, expected_damage, critical_strike


class Damage(Skill):
    def record(self, current_frame, player_id, skill_level, skill_stack, critical, parser):
        super().record(current_frame, player_id, skill_level, skill_stack, critical, parser)
        skill_tuple = (self.skill_id, skill_level, skill_stack)
        status_tuple = parser.available_status(player_id, self.skill_id)
        current_record = parser.records[player_id][-1]
        current_record[skill_tuple][status_tuple].append(
            (current_frame - parser.start_time[player_id][-1], critical)
        )
        return skill_tuple, status_tuple


class DotDamage(Damage):
    def record(self, current_frame, player_id, skill_level, skill_stack, critical, parser):
        skill_tuple, status_tuple = super().record(current_frame, player_id, skill_level, skill_stack, critical, parser)
        parser.last_dot[player_id][self.skill_id] = (skill_tuple, status_tuple)
        parser.ticks[player_id][self.skill_id] -= 1


class PetDamage(Damage):
    pass


class PhysicalDamage(PhysicalSkill, Damage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return PHYSICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class MagicalDamage(MagicalSkill, Damage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class MixingDamage(MixingSkill, Damage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_ATTACK_POWER_COF(super().attack_power_cof + self.interval)


class PhysicalDotDamage(PhysicalSkill, DotDamage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return PHYSICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)


class MagicalDotDamage(MagicalSkill, DotDamage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)


class MixingDotDamage(MixingSkill, DotDamage):
    @Damage.attack_power_cof.getter
    def attack_power_cof(self):
        return MAGICAL_DOT_ATTACK_POWER_COF(super().attack_power_cof, self.interval)
