day = 6

''' swither = {
    0 : 'Sunday',
    1 : 'Monday',
    2 : 'Tuesday'
} '''

def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'Unknown'

swither = {
    0 : get_sunday,
    1 : get_monday,
    2 : get_tuesday
}



# day_name = swither[day]
day_name = swither.get(day,get_default)()
print(day_name)
