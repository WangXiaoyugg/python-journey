# def curve_pre():
#     a = 25
#     def curve(x):
#         # y = ax^2 + bx +c 
#         return a*x*x 
#     return curve

# a = 10
# f = curve_pre()
# print(f(2))

# def f1():
#     a = 10
#     def f2():
#         # 局部变量不能影响到外部变量
#         # a变量不能被赋值，要应用外部的变量
#         a = 20
#         print(a)
#     print(a)
#     f2()
#     print(a)

# f1()      
 

# 旅行者 x =>  走三步  result = 3
# 再走5步，result = 8 ,在走6步 result = 14


# origin = 0
# def go(step):
#     global origin
#     new_pos = origin + step
#     origin = new_pos
#     return new_pos
# print(go(2))
# print(go(3))
# print(go(6))   

# origin = 0
# def factory(pos):
#     def go(step):
#         nonlocal pos
#         new_pos = pos + step
#         pos = new_pos
#         return new_pos
#     return go 

origin = 0
def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go 
f = factory(origin)

print(f(2))
print(f(3))
print(f(6))

