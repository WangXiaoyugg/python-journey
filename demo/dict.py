student = {
    'mike':18,
    'mary':20,
    'mali':34
}

# a = [key,value for key,value in student.items()]

# a = {value:key for key,value in student.items()}

a = (key for key,value in student.items())

for i in a:
    print(i)
# print(a)