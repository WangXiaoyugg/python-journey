import re

s = 'A8C3721D86E67'

def convert(value):
    matched = value.group()
    if int(matched) >= 6:
        return '9'
    else:
        return '0'



r = re.sub('\d',convert,s)
print(r)


# language = 'PythonC#JavaPHPC#C#'

# def convert(value):
    # matched = value.group()
    # return '!!'+ matched + '!!'    



# r = re.sub('C#',convert,language)

# print(r)


# language = language.replace('C#','GO')
# print(language)