# 列表推导式

a = [1,2,3,4,5,6,7,8]
b = [i**3 for i in a]

# a >= 5 的条件才平方，有条件筛选
c = [i**2 for i in a if i >= 5]
print(b)
print(c)

# set dict ,tuple 也可以被推导

x = {1,2,3,4,5,6,7,8}
y = {i**2 for i in x if i <= 5}
print(y)

h = (1,2,3,4,5)
j = (i+5 for i in h if i<=4)
print(tuple(j))