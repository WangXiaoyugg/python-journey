import re

a = 'C0C++8Java7#9Python5Javascript'

# 找数字
r = re.findall('\d',a)

# 找非数字
p = re.findall('\D',a)
print(r)
print(p)