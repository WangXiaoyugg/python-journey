'''
This is dir.py 
'''
a = 2
b = 3

infos = dir()

print(infos)
# 命名空间 + 模块名
print('name: ' +__name__)
# 包名
print('package: '+ (__package__ or '当前包没有模块'))
# 文件注释
print('doc: ' + __doc__) 

# 文件路径
print('file: '+__file__)
