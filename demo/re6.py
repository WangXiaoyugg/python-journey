import re

a = 'PythonPythonPythonPythonPython'

r = re.findall('(Python){3}',a)

print(r)