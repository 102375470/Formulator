from base.attribute import PhysicalAttribute
from base.constant import *


class FenShanJing(PhysicalAttribute):
    AGILITY_TO_ATTACK_POWER = 1751 / BINARY_SCALE

    def __init__(self):
        super().__init__()
        self.physical_attack_power_base += 3449
        self.physical_overcome_base += 1526
        self.pve_addition += 92

    @property
    def extra_physical_attack_power(self):
        return int(self.agility * self.AGILITY_TO_ATTACK_POWER)
