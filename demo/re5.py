import re

qq = '100011000'

r = re.findall('^\d{4,8}$',qq)

print(r)