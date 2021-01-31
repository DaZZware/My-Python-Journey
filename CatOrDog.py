# dog or cat to human calculator

catagory = input('Please type: cat or dog ')
if catagory == 'cat':
    age1 = input('Enter age of cat in human years using digits: ')
    age1 = int(age1)
    if age1 == '1':
        print('Your cat is 15 human years..')
    elif age1 == '2':
        print('Your cat is 24 in human years..')
    else:
        age2 = age1 * 4 - 8 + 24
        print('You cat is ', age2,'in human Years')
        human = input('Enter Your age in digits: ')
        human = int(human)
        human1 = human * 4 - 8 + 24
        print('To a cat you would be', human1, 'Years old!!! Scary is it?')
        input('Enter to Exit!')
else:
    age1 = input('Enter age of dog in human years using digits: ')
    age1 = int(age1)
    if age1 == '1':
        print('Your dog is 12 human years..')
    elif age1 == '2':
        print('Your dog is 24 in human years..')
    else:
        age2 = age1 * 4 - 8 + 24
        print('You dog is ', age2,'in human Years')
        human = input('Enter Your age in digits: ')
        human = int(human)
        human1 = human * 4 - 8 + 24
        print('To a dog you would be', human1, 'Years old!!! Scary is it?')
        input('Enter to Exit!')