from base.attribute import LunarAttribute
from base.constant import *


class BingXinJue(LunarAttribute):
    SPIRIT_TO_ATTACK_POWER = 1946 / BINARY_SCALE
    SPIRIT_TO_CRITICAL_STRIKE = 287 / BINARY_SCALE

    def __init__(self, platform=0):
        super().__init__()
        self.lunar_attack_power_base += 4222

    @property
    def extra_lunar_attack_power(self):
        return int(self.spirit * self.SPIRIT_TO_ATTACK_POWER)

    @property
    def extra_lunar_critical_strike(self):
        return int(self.spirit * self.SPIRIT_TO_CRITICAL_STRIKE)
