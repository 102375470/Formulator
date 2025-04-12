from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1922,): CriticalSet(GENERAL_BUFFS[4671]),
    (2759,): Gain(),
    (1938,): Gain(),
    (2421,): Gain(),
    **{(4940, level + 1): Gain() for level in range(8)},
    **EQUIPMENT_GAINS,
}
