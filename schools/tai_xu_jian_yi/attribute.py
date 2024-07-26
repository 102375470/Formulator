from base.attribute import PhysicalAttribute
from base.constant import *


class TaiXuJianYi(PhysicalAttribute):
    AGILITY_TO_ATTACK_POWER = 1485 / BINARY_SCALE
    AGILITY_TO_CRITICAL_STRIKE = 594 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.physical_attack_power_base += 3277
        self.physical_critical_strike_base += 2929
        self.platform = platform
        if not platform:
            self.pve_addition_base += 154
        else:
            self.pve_addition_base += 481
            self.all_shield_ignore += 614

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.AGILITY_TO_ATTACK_POWER)

    @property
    def extra_physical_critical_strike(self):
        return int(self.agility * self.AGILITY_TO_CRITICAL_STRIKE)

    @property
    def extra_pve_addition(self):
        if not self.platform:
            return 0
        else:
            return int(self.surplus_base / (3000 * 100) * BINARY_SCALE)
