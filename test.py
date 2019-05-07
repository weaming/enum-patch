#!/usr/bin/env python3

from enum import Enum
from enum_patch import patch
patch()


class Currency(Enum):
    USD = '$'
    HKD = 'HK$'


print("HKD" in Currency)
print(Currency.HKD in Currency)
print(list(Currency.iter_name()))
print(list(Currency.iter_value()))
