class Student():
    # 类变量
    # 一个班级所有学生总数
    sum1 = 0
    
    name = 'parent'
    age = 0


    # 类变量和实例变量
    # 实例方法
    # 构造函数
    def __init__(self,name,age):
        # 构造函数初始化类的特征
        # 实例变量        
        #只返回None
        self.name = name
        self.age = age
        self.score = 0
        # print(age) # 指传入的形参
        # print(name) # 指 的是传入的形参
        # print(Student.sum1)
        self.__class__.sum1 += 1
        print('当前的班级学生总数：'+ str(self.__class__.sum1))
    
    def do_homework(self):
        self.do_cook()
        print('homework')
    
    def __marking__(self,score):
        if score < 0:
            return '不能给学生打负分'
        self.score = score
        print(self.score)


    # 类方法
    @classmethod
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)
    
    @staticmethod
    def add(x,y):
        print(Student.sum1)
        print(x,y)
        print('This is a static method')   

    def do_cook(self):
        print('do cook')

student1 = Student('mary',20)
res = student1.__marking__(-1)
print(res)

''' Student.add('1','2');
student1 = Student('mary',20)
Student.plus_sum();
student1 = Student('mike',20)
Student.plus_sum(); '''










# print(student1.do_homework())
# print(student1.__dict__)
# print(Student.__dict__)