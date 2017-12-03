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