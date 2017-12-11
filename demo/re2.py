import re

s = 'abc,acc,adc,aec,afc,ahc'

# 匹配 acc 或 afc

r = re.findall('a[cf]c',s)

# 不匹配 acc 和 afc

p = re.findall('a[^cf]c',s)

# 匹配 acc adc aec afc
w = re.findall('a[c-f]c',s)
print(r)
print(p)
print(w)