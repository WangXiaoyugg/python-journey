import json

json_str = '{"name":"qiyue","age":18}'
json_array = '[{"name":"qiyue","age":18,"flag":false},{"name":"qiyue","age":18}]'
std1 = json.loads(json_array)
print(type(std1))
print(std1)

# std = json.loads(json_str)

# print(type(std))
# print(std)
# print(std['name'])
# print(std['age'])
