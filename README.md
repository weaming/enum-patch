Patch the python3's `enum.Enum`.

```
from enum import Enum
from enum_patch import patch
patch()


class Currency(Enum):
    USD = 1
    HKD = 2


print("HKD" in Currency)
print(list(Currency.iter_str()))
```
