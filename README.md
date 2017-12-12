# python-journey

## 开始学习pyhton 之旅

### 第一天

1. 安装python很简单，[下载地址](https://www.python.org/downloads/)
   windows点击安装包，默认下一步下一步结束
2. python [官方文档](https://docs.python.org/3/)
3. IDLE 交互练习，mac在终端输入 python 按 回车, 打印hello world
`print('hello,world')` 

4. 代码是什么，怎么写代码
- 代码是实际世界的事物的映射
- 写代码用计算机语言来描述现实世界的🍜
- 计算机语言，基本数据类型

5. 数字 Number
- 整数 int
- 其他语言整数 short, int,long
- 浮点数 float ,python 默认 双精度
- 其他语言浮点数单精度 float, 双精度 double   
```
type(1)
type(1.1)
type(1.1111111)
type(1 + 0.1)
type(1+1)

type(1 + 1.0) float
type(1 * 1) 
type(1 * 1.0) 
type(2/2) float 重点 在 python2.7 版本里是 int
type(2//2) int
2/2 = 1.0
2//2 = 1
1//2 = 0  保留整数部分
```
- 10，2，8，16进制
满 10 进 1 ， 满 2 进 1 ， 满 8 进 1 ， 满 16 进 1
[0 - 9]       [0-1]      [0-7]       [0-9A-F]
- 各种进制的表示
```
0b10  二进制
0o10  八进制
0x1F  十六进制
```
- 各种进制转换
```
bin(10) => 0b1010
bin(0o7) => 0b111
bin(0xE) => 0b110
int(0b11) => 3
int(0o77) => 77
hex(10) =>  0xa
hex(0o777) => 0x1ff
oct(0b111) => 0o7
oct(0x777) => 0o3567
```
- bool类型，true,false
- complex 复数
```
True   大写
False  大写
type(True)
type(False)
int(True)  1
int(False) 0
bool(1)  True
bool(0)  False
bool(2) True
bool(2.2) True
bool(-1.1) True  非 0 都是 布尔真，0表示 布尔假
bool('abc') True
bool('') False
bool([1,2,3]) True
bool([]) False
bool({1,1,1}) True
bool({}) False
bool(None) False
非空一般被认为 True, 空值被认为 False 

2j 表示复数
```
6. 字符串
- 单引号 ''
- 双引号 ""
```
"let's go"
'let"s go'
'let\'s go' 转义字符 \ 
```
- 引号要成对出现
- 多行字符串 >79个字符要换行  ''' '''
```
''' hello
hello
hello
'''
\n  回车
""" hello world \n hello world \nhello world \n""" IDLE不会换行
print(""" hello world \n hello world \nhello world \n""") 会换行
```
- 转义字符
```
\n 换行
\' 单引号
\t 横向制表符
\r 回车

print("hello \n world") \n 不消失
print("hello \\n world")
print('c:\my\project') 不换行
print('c:\\my\\project')
print(r'c:\my\project') 原始字符串加 r
```
- 字符串操作运算
```
'hello' + 'world' 拼接字符串
‘hello’ * 3  =>  'hellohellohello'
'hello world'[0] => h
'hello world'[3] => l
'hello world'[-1] => d
'hello world'[-3] => r 下标正数顺序，负数倒序
'hello world'[0:4] => 'hell'
'hello world'[0:5] => 'hello' 最后截取的下一位
'hello world'[0:-1] => 'hello worl'
'hello world'[0:-3] => 'hello wo'
'hello world'[6:] => 'hello'
'hello python java c# javascript php ruby'[-4:] => ruby
'hello python java c# javascript php ruby'[:-4] => 'hello python java c# javascript php '
R'C:Windows' => 'C:Windows'
```
### 第二天

#### 基本类型-组
1. 列表,内部数据类型任意
`type([1,2,3,4,5,6]) list`
`['hello',True,1]`
`[[1,2],[2,3],[True,False]] 嵌套列表`
2. 列表操作
```
//get
['汽车','火车','飞机','轮船'][0] string
['汽车','火车','飞机','轮船'][3] string
['汽车','火车','飞机','轮船'][0:2] list[]
['汽车','火车','飞机','轮船'][-1:] list[]

//add
['汽车','火车','飞机','轮船'] + ['火箭','飞船'] => ['汽车','火车','飞机','轮船','火箭','飞船']
['火箭','飞船'] * 3  => ['火箭','飞船','火箭','飞船','火箭','飞船']

[['巴西','克罗地亚','美国','英国'],[],[],[],[],[],[],[],[]]
```
3. 元组
```
(1,2,3,4,5)
(1,'1',True)
(1,2,3,4,5)[0]
(1,2,3,4,5)[0:2]
(1,2,3) + (4,5,6)
(1,2,3) * 3

type((1,2,3)) tuple
type([1,2,3]) list
type('hello') str
type(1)       int

type((1))     int
type(('hello')) str
type((1)) => type(1) => int

只有一个元素的元组
type((1,))

空元组
type(())
```
4. 序列
- str , list, tuple
- [下标]获取元素，每个序列的元素有下标序号
- [0:3]切片 `'hello world'[0:8:2]`
- 序列可以 + *
```
3 in [1,2,3,4,5,6] True
3 not in [1,2,3,4,5,6] False
len([1,2,3,4,5,6]) => 6
len('hello') => 5
max([1,2,3,4,5]) => 5
min([1,2,3,4,5]) => 1

//字母按 按 acsll 码 排序
max('hello world') => w  
min('helloworld') => d
ord('w') 119
ord('d') 100
ord(' ') 32

```
5. 集合
```
type({1,2,3,4,5,6}) set
//无序没有索引
{1,2,3,4}[0] 报错
{1,2,3}[0:1] 报错

//自动去除重复元素
{1,1,2,2,3,3} => {1,2,3}

1 in {1,2,3,4} True
1 not in {1,2,3} False
len({1,2,3}) 3 

// 减号求两个集合的差值
{1,2,3,4,5,6} - {3,4} => {1,2,5,6} 

// & 两个集合的交集
{1,2,3,4,5,6} & {3,4} => {3,4}

// | 两个集合的并集
{1,2,3,4,5,6} | {4,5,6,7,8} => {1,2,3,4,5,6,7,8}

//空集合
type({}) dict
type(set()) set
len(set()) 0   
```
6. 字典
- key : value
- 字典可以有很多的value 和 key, 是集合的一种
```
type({key1:val1,key2:val2}) set
type({1:1,2:2,3:3}) dict
{
    'q':'新月打击',
    'w':'苍白之瀑',
    'e':'月之降临',
    'r':'月神冲刺'
}
```
- 通过key 访问 value
```
//字典不能有重复的key
{
    'q':'新月打击',
    'w':'苍白之瀑',
    'e':'月之降临',
    'r':'月神冲刺'
}[q]
{
    'q':'新月打击',
    'q':'苍白之瀑',
    'e':'月之降临',
    'r':'月神冲刺'
}[q] => '苍白之瀑'

//key 可以是数字,字符串,元组 ,必须是不可变的数据类型 ，value: str int list set dict

//空的字典 怎么定义
type({}) dict

```
7. 小结
- 数字(int,float, bool,complex)
- 组  
  1. 序列(str,list,tuple) 有序，可以用下标索引来访问，支持切片操作，不可变
  2. 集合(set) 无序，无索引，不能切片
  3. 字典(dict) key:value 键值对

### 第三天

#### 变量和运算符
1. 什么是变量？一组数据的名字
```
a = [1,2,3,5,6]
print(a)
b = [1,2,3]
a*3 + b + a

//变量名必须有意义
skill = ['eat','drink']

```
2. 变量命名规则
- 字母，数字，下划线，且不能以数字开头
- 系统保留关键字不能用在变量名中
- 变量名事区分大小写
- 变量没有类型限制

3. 值类型和引用类型
```
//值类型(不可改变) int str tuple
a = 1
b = a
a = 3

//引用类型（可变） list set dict
a = [1,2,3]
b = a
a[0] = '1'

//生成新的变量，内存地址不同
a = 'hello'
id(a)
a = a+ 'world'
id(a) 

```
4. 列表的可变和元组的不可变
```
代码稳定性 => 元组
a = (1,2,3,[1,2,[a,b,c]])
a[3][2][1] => b

a = (1,2,3,[1,2,4])
a[3][2] = '4'  改变的是元组

```
5. 运算符号
```
+ - * / //
%  
2**2  => 4
2**3  => 8

赋值运算符
= —= += /= %= //= *= **=
c = 1
c = c + 1  => c += 1 => c++ 报错 python 不支持

关系运算符 返回值是布尔值
==  != > < >=  <=
1 == 1 True
1 > 1 False
1 >= True
1 != 2 True

b = 1
b += b>=1 => b = b+ True => b = b+1 => b = 2
'a' > 'b' False  比较的 ascii 码的大小
'abc' < 'abd' True
[1,2,3] < [1,2,4] True
(1,2,3) < (1,3,2) True


逻辑运算符 => 操作类型和返回类型都是布尔类型
and or not
and 且
or 或
not 取反，操作一个变量

1 and 1  => 1
'a' and 'b' => b
'a' or 'b' => a
not 'a' => False

int float  0 被认为是False, 非 0 表示 True
not 0.1 False

str  空字符串 False,其他的是 True
not '' True

list [] False, 其他的是 True
元组同 list

[1] or []  => [1]
[] or [1] => [1]

'a' and 'b' => 'b'
'' and 'b' => ''
 
1 and 2  => 2
1 or 2  => 1
0 and 1  => 0
1 and 0 => 0
0 or 1 => 1
1 or 1 => 1

 
成员运算符 一个元素是否在另一个元素里，返回的是布尔值
in not in
a = 1
a in [1,2,3,4,5] True
a not in [1,2,3] False
b = 6
b in [1,2,3,4,5]

b = 'a'
b in {'c':1} False
b = 1
b in {'c':1} False
b = 'c'
b in {'c':1} True

身份运算符 返回的是布尔值
is is not

a = 1
b = 2
a is b False
a = 1
b = 1.0
a == b  True
a is b  False 
is 比较两个变量的内存地址是否相等
not is 比较两个变量的内存地址是否不相等

a = {1,2,3}
b = {2,1,3}
a == b True
a is b False

c = (1,2,3)
d = (2,1,3)
c == d False
c is d False

a == b 值判断
a is b  身份判断
type a  类型判断

a = 'hello'
type(a) == int
type(a) == str

//判断变量类型,推荐使用，可以判断对象的子类，而type不可以
isinstance(a,str) => True
isinstance(a,(int,str,float)) => True
isinstance(a,(int,float)) => False

对象有三个特征 id,value,type

位运算符
& | ^ ~ << >> 把数字当作二进制数字处理
& 按位与
| 按位或
~ 按位异或
<< 左移动
>> 右移动

10  
&    =>  1 0  => 2
11

10
|  =>   11 => 3
11


```

### 第四天

#### 表达式
1. 表达式是运算符和操作数所构成的序列
```
c = int('1') + 2

a = 1 
b = 2
c = 3
a + b * c => 7
a or b and c  =>  a or (b and c) => 1
```
2. 运算符的优先级
- 同级的从左到右  => 左结合
- () 的优先级最高
- 赋值运算符 =  从右到左 => 右结合
```
a = 1
b = 2
c = 2

not > and > or
not a or b + 2 == c
(not a) or  ((b+2) == c))
```
3. 在文件编写代码
- 编码工具 IDE pycharm
- 编辑器  vscode sublime
- 编写代码保存为 xxx.py
- 在终端里找到对应的目录 使用命令 python xxx.py

4. vscode 开发环境和python 插件安装
- 插件 python termial vim veiw in browser vscode-icons
- 编辑器具备的三个功能：智能感知，调试，语法检测

5. 流程控制语句
- 缩进表示代码块
- if else for while
- 注释 # 单行 ， 多行注释 ''' '''
- python 不可以混淆和压缩，因为缩进语法 
- 变量名用 _ 分隔
- 使用 pylint 检查 代码
```
todo 
1. 切换系统默认的python版本 为 3.6.2 而不是 2.7.1
2. pylint 的版本 切换为 3.6.2, 而不是 2.7.1
```
6. snippet ,嵌套分支，代码块
- snipppet 代码块
- pass 占位
- 代码块
- if else 嵌套，把内层的if- else 封装函数，减少嵌套
- elif 减少判断
- python 中为什么没有 switch case [文档地址](https://docs.python.org/2/faq/design.html#why-isn-t-there-a-switch-or-case-statement-in-python)
```
python 官方认为 switch case 你可以用 if elif else 代替
但是python switch case 还没有一致认同的方案以及怎么进行范围测试
官方例子：
假若你要从非常多的数字中选择符合条件的，你可以创建一个字典，然后使map字典的值去调用
def function_1(...):
    ...

functions = {'a': function_1,
             'b': function_2,
             'c': self.method_1, ...}

func = functions[value]
func()

除了 使用对象的方法进行调用，你也可以简单使用pyhton内部方法getattr()去调用特定名字的方法
def visit_a(self, ...):
    ...
...

def dispatch(self, value):
    method_name = 'visit_' + str(value)
    method = getattr(self, method_name)
    method()
python 官方建议给方法名添加后缀 ，如 visit_, 没有这样的后缀_，假若值来自一个不可靠的数据源
攻击者可以轻松调用 你的对象的任意方法    
```
- 不报错代码结果不符合预期，注意变量的数据类型是否改变
```
# a b 不能同时为False
if（ a != False or b !== False)
    print('xxx')
可以简写成  a or b    
```

### 第五天

#### 循环
1. while else 知道一个目标，达到目标就退出
2. for 主要用来遍历 序列，集合，字典 break,continue
3. range(0,10) =>  0 - 9  rang(10,0,-2)
4. 会写代码，很容易，写出高性能，封装性(可复用)代码很难
5. 写代码考验抽象能力
6. 代码优美,高性能，封装性(可复用)

### 第六天

#### 包，模块，类
1. 包(文件夹) > 模块(xxx.py) > 类(写在xxx.py里面) > 函数/变量
2. 包和模块的名字
```
相同的模块不同的包，加上包的名字，命名空间
包可以有子包
包文件夹下面必须有 __init__.py  => 模块名就是 包的名字
```
3. import 必须先定义，才能使用，导入的是一个模块，包的嵌套时必须加上 命名空间
```
import xxx.xx.xx as x
print(x.m);

导入具体变量，函数，不需要命名空间
from t.c7 import a
print(a)
from t.ct import *

# * 导出所需的变量，函数,__all__ 内置模块
__all__ = ['a','c'] 

__pycache__ 文件夹是python 编译的二进制文件的缓存，
```
4. __init__.py 的用法
- vscode设置 files.exclude ,__pycache__ true
- 导入多个模块
```
from c9 import a,b,c

导入的模块特别多,需要换行
from c9 import a,b,\
c
from c9 import (a,b,
c)

print(a)

```
- 当一个包被导入的时候，包的 __init__.py 会被首先执行
- __init__.py 的使用场景
```
xxx包
__init__.py 文件

决定哪些模块被导入，决定包可以使用哪些模块
__all__ = [a,b,c]

公共使用的内置模块，sys,io,date
在__init__.py 中引入
import sys
import io
import date

在其他模块中使用内置的模块
impory xxx.sys

```
- 包和模块不会被重复导入
- 避免循环导入,避免多个文件的循环引用
```
p1.py
from p2 import p2
print(p2)

p2.py
from p1 import p1
print(p1)
```
- 一旦导入模块，会执行模块的代码
- 应用程序只有一个入口文件

5. 模块的内置变量
```
print(dir())
```
6. 入口文件
- __package__ 为 NoneType
- __name__ 为 __main__
- __file__ 为 文件名

7. __name__ 的使用场景
```
import sys
infos = dir(sys)
print(info)

if __name__ == '__main__':
    print('This is app')
print('This is module')

//doc 文档自动生成工具
遍历 每个文件 __doc__

//成为模块必须在包目录下面
python -m demo.dir.py    
```
8. 相对导入和绝对导入
```
目录结构
DEMO
- package1
- package2
- package3
- main.py 决定顶级包的位置

绝对导入必须从顶级包开始

相对导入
from ..m4 import m
from .m1 import n

from ...m5 import n
valueerror,试图去引入超过顶级包的模块?
把m5放入 package2 内

main.py 是入口文件 ，是不能使用相对导入

如果非要把 main.py 当模块使用, 使用相对导入

执行换到上一级目录
python -m demo.main

```

### 第七天

#### 函数

1. 函数
```
print()
a = 1.2386
print(round(a,2))
```
- 功能性
- 封装性
- 复用性
- 组织代码

2. 函数定义和运行特点
```
def xxx():
    xxx = 'xxx'
    return xxx:

def xxxx():
    print('xxxx')    
```
3. 函数返回多个值，遇到return 就终止了
4. 序列解包,两边元素要相等
```
a = 1
b = 2
c = 3

a,b,c = 1,2,3

d = 1,2,3
print(type(d)) tuple

a,b,c = d

a = 1
b = 1
c = 1

a = b = c = 1
a,b,c = 1,1,1

```
5. 必须参数和关键字参数
- 必须参数必须传入，不传入报错
- 形参和实参
- 关键字参数，不考虑参数的顺序,在传递实参的时候

6. 默认参数
```
def add(a,b=1,c=2):
    return a+b+c

add(1)
add(1,2)
add(1)
一般要遵守顺序
使用关键参数可以不遵守顺序
add(1,c=10)


```
7. 可变参数
```
def demo(*param):
    print(param)
    print(type(param)) // tuple

demo(1,2,3,4,5,6)    
demo((1,2,3,5,6)) //((1,2,3,4,5))

a = (1,2,3,4,5,6)
demo(*a) //(1,2,3,4,5,6)

def demo(param1,param2=2,*param):
    print(param1)
    print(param2)
    print(param)

demo('a',1,2,3 ) // a 1 (2,3)

def demo(param1,*param,param2=2):
    print(param1)
    print(param2)
    print(param)

demo('a',1,2,3,'param')
// a (1,2,3,'param') 2

demo('a',1,2,3,param2='param')
// a (1,2,3) 'param'

```
- 保证函数参数类型的简单

8. 关键字可变参数 
```
def sum(*param):
    sum = 0
    for i in param
        sum += i * i
    print(sum)

sum(1,2,3,4,5,6)

def city_temp(**param):
    for key,value in param.items():
        print(key,':',value)

city_temp(bj='32',xh='23c',sh='32c') //dict 类型       

a = {'bj':'32','xh':'23c' ,sh:'32c'}
city_temp(**a)
```
9. 变量的作用域
```
c = 50  // 全局变量

def add(x,y):
    c = x + y  //局部变量
    print(c)

add(1,2)  // 3
print(c) //50

# 没有块级作用域，for 循环的变量和函数的变量是同一层级

# 作用域链，层级寻找
c = 1
def func1():
    c = 2
    def func2():
        c = 3
        print(c)
    func2()

func1()        
```
10. global 关键字,成为全局变量
```
def demo():
    global c 
    c = 2

demo()
print(c)    
```
11. 练习题
```
游戏的经济系统
五行石的合成  1 - 8 级
来源 自己合成 ，其他玩家购买
市场货币:金币
五行石 合成 金币，钻石，体力

目标得到 6级五行石
1. 1级 五行石 消耗金币和钻石
2. 1级 => 3级 五行石 12个1级， 

```
### 第八天

#### 类和面向对象
1. 类和 实例化
```
class Student():
    name = ''
    age = 0

    def print_file(self):
        print('name: '+ self.name)
        print('age: '+ str(self.age))

student = Student()
student.print_file()
```
2. 类的基本作用:封装
3. 模块功能单一，要么定义类，要么执行类
4. 方法和函数的区别
- c, C++ 叫函数，面向过程的概念，不定义在类里
- java ,C# 叫方法，面向对象的概念，设计层面，定义类里，
- 变量在类里叫数据成员，不在类里叫变量
5. 类和对象
- 类定义特征和行为
- 类实例化就是对象
6. 构造函数
7. 局部模块中的变量和类中的变量
8. 实例变量和类变量(类共有的变量)
9. 类与对象的变量查找顺序
10. self 和 实例方法
- self 类似 this ,self 可以改为 this
- 强制要求在方法定制第一个参数为 self
- self就是当前调用方法的实例
11. 实例方法访问实例变量和类变量
```
python 类
    - 变量
        - 类变量
        - 实例变量
    - 方法
        - 实例方法
        - 类方法
        - 静态方法
    - 构造函数
    - 成员的可见性
        - 公开
        - 私有
    - 面向对象的3大特性
        - 封装性
        - 继承性(最难)
        - 多态性    
```
```
print(Student.sum1)
print(self.__class__.sum1)

@classmethod
def plus_sum(cls):
    cls.sum += 1
    print(cls.sum)

@staticmethod
    def add(x,y):
        print('This is a static method')   


Student.plus_sum()

# 其他语言
public name
private sum

python
方法和变量以 __ 开头，构造函数除外 __init__
student1.__score = -1  # 不是不报错，而是新增了一个属性  
print(student1.__score)

print(student2._Student__score)
```
12. 静态方法尽量可以类方法代替
13. 对类的成员的变量赋值通过方法，可以做校验，不要直接赋值
14. python的私有变量 __score 更换为 _Student__score
15. 继承， 学生的类 继承 人的类
- python 可以单继承和多继承
16. 子类调用父类的方法
```
People.__init__(self,name,age)
# 关键字super 调用父类
super(Student,self).__init__(name,age)
super(Student,self).do_homeword()
```
- 开闭原则，对类的更改的是封闭的

### 第九天

#### 正则表达式

1. 正则表达式定义
- 正则表达式是一个特殊的字符序列，一个字符串是否与我们所设定的这样的字符序列是否匹配
- 实现文本检索，文本替换
```
import re

a = 'C|C++|C#|Python|Java|Javascript'
r = re.findAll('python',a)
print(r);
```
- 正则表达式的灵魂是规则
2. 元字符和普通字符
```
普通字符
'Python'

元字符 重点
\d  匹配数字字符 [0-9]



```
3. 概括字符集
4. 数量词
- * 0次或多次
- + {1,}
- ? {0,1}
5. 贪婪和非贪婪
- 贪婪就是尽可能匹配更多，默认的
- 非贪婪，在数量词后面加 ？
6. 边界匹配 ^ $
7. 组 ()
8. 匹配模式 re.I re.S
9. re.sub 正则替换
- 把函数作为参数传递
10. re.match
11. re.search
12. group 分组
13. python 主要应用场景 爬虫，数据分析和处理
- 电话号码校验
- qq校验
- 工作上使用别人写好的表达式，效率高
- 学习上多使用正则表达式

### 第十天

#### JSON
1. 什么事JSON
- JSON - Javascript Object Notation
- 轻量级的数据交换格式
- JSON字符串符合JSON的数据格式
- XML 也是数据交换格式

2. 优点
- 易于阅读
- 跨语言交换数据
- 易于解析
- 网络传输效率高

3. 使用场景
- 网站后台 => JSON  => 浏览器
- 不同语言服务的JSON 数据交换

4. python中使用JSON
5. 反序列化，把json字符串转化成对应的数据结构
6. 序列化 
7. JSON 对象,JSON,JSON字符串
- JSON 是 基于 ECMA规范生成的 ，不是javascript的附属品
- JSON 有自己的数据类型
- 中间语言的数据交换格式
- REST服务使用json