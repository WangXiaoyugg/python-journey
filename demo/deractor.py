import time


def f1():
    print('this is a function1')
# unix 时间戳
# f1()

# 对修改式封闭的，对扩展式开放的

def f2():
    print('this is a function2')


def print_current_time(func):
    print(time.time())
    func()

print_current_time(f1)
print_current_time(f2)        