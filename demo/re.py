import re

a = 'C|C++|C#|Python|Java|Javascript'
# r = re.findall('Python',a)


# if len(r) > 0:
#     print('字符串包含PHP')
# else:
#     print('No')

''' if (a.index('Python') != -1):
    print('字符串包含python')
else:
    print('No') '''


if ('Python' in a ):
    print('字符串包含python')
else:
    print('No')    
