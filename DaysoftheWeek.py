# Day of the week
day =input('Enter the Day of the week :')
if day == 'monday' or day == 'wednesday':
    alarm = '7.30am'
    carpool = True
    coding_Class = True
    gym = False
elif day == 'tuesday' or day == 'thursday':
    alarm = '7.30am'
    carpool = False
    coding_Class = False
    gym = True
elif da == 'friday':
    alarm = '6.30am'
    carpool = True
    coding_class = False
    gym = False
else:
    alarm = 'OFF'
    carpool = False
    coding_Class = False
    gym = True
print('Alarm: ',alarm,' Carpool: ',carpool,' Coding Class: ',coding_Class, ' Gym: ',gym)

input()
