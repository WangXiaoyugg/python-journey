from cls1 import People

class Student(People):
    ''' sum = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum +=1 '''

    def __init__(self,school,name,age):
        self.school = school
        # People.__init__(self,name,age) #调用父类的构造函数    
        super(Student,self).__init__(name,age)


    def do_homework(self):
        super(Student,self).do_homework()
        print('do homework')

std1 = Student('ANHUI UIVERSITY','mike',20)
# print(std1.sum)
# print(Student.sum)
print(std1.name)
print(std1.age)
std1.do_homework()
# std1.get_name()
