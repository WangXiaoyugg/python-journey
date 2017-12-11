import re

''' s = '83C&2D1D8E67'
r = re.match('\d',s)
print(r.span())

r1 = re.search('\d',s)
print(r1.group()) '''

s = 'life is short,i use python,i love python'

r = re.search('life(.*)python(.*)python',s)
# print(r.group(0))
# print(r.group(1))
# print(r.group(2))
print(r.groups())
print(r.group(0,1,2))
