# 装饰器
import time

def decorator(func):
    def wrapper(*args,**kw):
         print(time.time())   
         func(*args,**kw)   
    return wrapper 

# 装饰器没有改变函数原来的调用方式
# 装饰器利用可变参数，解决参数不一致的问题
# 不知道参数是什么，抽象用 *args，**kw
@decorator
def f1(func_name):
    print('this is a function ' + func_name)

# f = decorator(f1)
# f()
@decorator
def f2(func_name1,func_name2):
    print('this is a function ' + func_name1)
    print('this is a function ' + func_name2)

@decorator
def f3(func_name1,func_name2,**kw):
    print('this is a function ' + func_name1)
    print('this is a function ' + func_name2)
    print(kw)


f1('func1')
f2('func1','func2')
f3('test func1','test func2',a=1,b=2,c='123')

# flask @api.route 验证身份
