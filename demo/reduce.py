from functools import reduce
list_x = [1,2,3,4,5,6]

# 连续计算，连续调用lambda
# (((1+2)+3) +4) + 5
r = reduce(lambda x,y:x+y,list_x,10)
print(r)

# (x,y) => (0,0) => (1,3) => (2,-2) => (-2,3)
# 计算最终的位置
# map /reduce  大数据编程模型 映射 归约 并行运算
