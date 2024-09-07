from base.gain import Gain
from general.buffs import GENERAL_BUFFS
from general.gains.equipment import EQUIPMENT_GAINS, CriticalSet

GAINS = {
    (1914,): CriticalSet(GENERAL_BUFFS[1439]),
    (2418,): Gain(),
    (1931,): Gain(),
    **EQUIPMENT_GAINS,
}
