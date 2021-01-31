# Adventure Game

import time


print('Wleomce to the Santa Cruz Mountain Adventure Game!')
print('*************************************************')
print('You are visiting Santa Cruz, California.')
print('You go on an evening hike alone in the mountains.')
print('You pick one item to take with you - ')
print('map(m), Flashlight(f), chocolate(c), rope(r), or stick(s): ')
item = input('What do you choose?: ')
time.sleep(3)
print('You hear a humming sound.')
choice1 = input('Do you follow the sound? Enter y or n: ')
if choice1 == 'y':
    print('You keep moving closer to the sound.')
    print('The sound suddently stops.')
    print('You are now LOST! ... ')
    print('You try to call on your phone, but there is no signal!')
    direction = input('Which direction do you go? north, south east, or west: ')
    if direction == 'north':
        print('You reach an abandoned Cabin.')
        if item == 'm':
            print('You use the map and find your way home.')
            print('CONGRADULATIONS! You won the game. ')
        else:
            print('If you had a map, you could find your way home from here.')
            print('---You are still lost. You lost the game.---')
    elif direction == 'south':
        print('You reach a river with a broken bridge.')
        if item == 'r' or item == 's':
            print('You chose an item that can fix the bridge.')
            print('You fix the bridge, cross over the river, and find your way home.')
            print('CONGRADULATIONS! You won the game.')
        else:
            print('If you had a rope or a stick, you could have fixed the bridge')
            print('---You are still lost. You lost the game.---')
    elif direction == 'west':
        print('You are walking and trip over a fallen log.')
        print('You have hurt your foot. You sit down and wait for help.')
        print('This could be a long time. You are still lost.')
        print('---You lost the game---')
    else:
        print('You reach the side of the highway. It is dark.')
        if item == 'f':
            print('You use the flashlight to signal for help')
            print('A car stops and gives you a ride home.')
            print('CONGRADULATIONS! You have got out safely. You have won the game.')
        else:
            print('If you had a flashlight, you could have signalled for help.')
            print('---You are still lost. You lost the game.---')
else:
    print('Good idea. You are not taking risks. ')
    print('You start walking back to the starting point.')
    print('You realize you are LOST! ... ')
    print('The sound is behind you and is getting louder. You panic! ')
    action = input('Do you start running (r), stop to make a call (c):? ')
    while action == 'c':
        print('The call does not go through')
        action = input('Do you want to run (r), or try calling again (c)?: ')
    print('You are running fast. The Sound gets really loud.')
    time.sleep(3)
    print('A woman on an electric scooter comes up behind you.')
    answer = input('She says, "Name my favourite computer programming language." ')
    if answer.lower() == 'python':
        print('She says, "Yes python is my favourite programming language."')
        print('"If you have any chocolate. I can help you."')
        if item == 'c':
            time.sleep(3)
            print('Luckily you did choose chocolate.')
            print('You give her the chocolate.')
            print('She helps you get home.')
            print('CONGRADULATIONS! You have won the game.')
        else:
            print('You should have chosen chocolate.')
            print('She rides away, leaving you alone and lost.')
            print('You lost the game')
    else:
        print('She did not like your answer.')
        print('She rides away, leaving you lost!')
        print('You lost the game')

input()
