from enum import Enum
from enum import IntEnum,unique

@unique
class VIP(IntEnum):
    YELLOW = 1
    GREEN = 1
    BLACK = 3
    RED = 4

# class VIP1(Enum):
#     YELLOW = 1
#     YELLOW_ALIAS = 1
#     BLACK = 3
#     RED = 4

# for v in VIP1.__members__.items():
#     print(v)

# a = 1
# print(VIP(a))



# print(VIP1.GREEN)
# 数值相等，枚举的别名

# 枚举的意义重在标签，而不是数值
# print(type(VIP.YELLOW))
# print(VIP.YELLOW.value)    
# print(type(VIP.YELLOW.name))
# print(VIP['GREEN'])

# for v in VIP:
#     print(v)

# result = VIP.GREEN is VIP1.BLACK

# print(result)
