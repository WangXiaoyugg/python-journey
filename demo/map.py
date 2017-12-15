
# 抛物线有很多点，已知 x 求 y
list_x = [1,2,3,4,5,6]
# list_y = [1,4,9,16,25,49,64]
list_z = [1,3,4,5,6,7,8]

# def square(x):
#     return x * x
# for in list_x:
#     square(x)

# r = map(square,list_x)
# print(r)
# print(list(r))

r = map(lambda x,z: x*x + z,list_x,list_z)
print(list(r))
