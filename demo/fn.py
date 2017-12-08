''' 
1. 参数列表可以没有
2. return value None
'''

''' import sys
sys.setrecursionlimit(1000) '''

def add(x,y):
    result = x + y
    return result

# 自己调用自己，递归默认最大 995 次，可以自己设置
# 避免和内置变量和函数名称相同
def print_code(code):
    print(code)


a = add(1,2)
b = print_code('python')

print(a,b)