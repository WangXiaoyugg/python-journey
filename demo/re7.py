import re
# . 匹配除 \n 的一切字符
# re.S 匹配一切字符

language = 'Python C#\n Java PHP'
r = re.findall('c#.{1}',language,re.I|re.S)
print(r)