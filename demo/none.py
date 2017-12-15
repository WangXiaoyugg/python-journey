# none != 空字符串 空列表 0 False

# a = ''
# b = False
# c = []

# print(a == None)
# print(b == None)
# print(c == None)

# print( a is None)
# print(type(None))

# def fun():
#     return None
# a = fun()
# a = []
# if not a if a 更好
# if not a:
#     print('False')
# else:
#     print('True')    

# if a is None:
#     print('False')
# else:
#     print('True')
# 

# 自定义的对象 
# bool 优先级高于 len
class Student():
    def __len__(self):
        return True
    def __bool__(self):
        return False


test = Student()
print(bool(Student()))
# print(len(Student()))
# print(bool(test))
# if test:
    # print('S')    
# else:
    # print('T')

    