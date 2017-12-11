import re

a = 'python 111 java 678php'
b = 'pytho0python1pythonn2'

p = re.findall('python{1,2}?',b)
print(p)

''' r = re.findall('[a-z]{3,6}?',a)
print(r) '''