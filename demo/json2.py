import json 
std = [
    {'name':'quexi','age':18,'flag':False},
    {'name':'quexi','age':18}
]

# NOSQL  MongoDB 可以存对象
# 不建议序列化后存到数据库

std = json.dumps(std)
print(type(std))
print(std)