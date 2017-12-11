# 概括字符集
import re

# \w 单词字符 [A-Za-z0-9_] 
# \W 非单词字符  \t & \n \r
# \s 空白字符 
# \S 非空白字符
a = '_python\t\n\r1111java&678php'

r = re.findall('\S',a)

print(r)
