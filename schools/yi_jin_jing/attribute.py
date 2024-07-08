from base.attribute import MagicalAttribute
from base.constant import *


class YiJinJing(MagicalAttribute):
    SPUNK_TO_ATTACK_POWER = 1894 / BINARY_SCALE
    SPUNK_TO_CRITICAL_STRIKE = 389 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.magical_attack_power_base += 4139
        self.pve_addition += 103

    @property
    def extra_magical_attack_power(self):
        return int(self.spunk * self.SPUNK_TO_ATTACK_POWER)

    @property
    def extra_magical_critical_strike(self):
        return int(self.spunk * self.SPUNK_TO_CRITICAL_STRIKE)
