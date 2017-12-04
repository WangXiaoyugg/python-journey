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



