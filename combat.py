# git them dials
import example_dials

error = 'what the fuck did you do?'
action = 'none'
t1c1 = batman
team = [t1c1.name]
target = team[0]

# allow program to clear in terminal after every turn 
from os import system, name
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 


while action != 'end':

#determine current click
    if t1c1.click == 1:
        curr = t1c1.one
    elif t1c1.click == 2:
        curr = t1c1.two
    elif t1c1.click == 3:
        curr = t1c1.three
    elif t1c1.click == 4:
        curr = t1c1.four
    elif t1c1.click == 5:
        curr = t1c1.five
    elif t1c1.click == 6:
        curr = t1c1.six
    elif t1c1.click == 7:
        curr = t1c1.seven
    elif t1c1.click == 8:
        curr = t1c1.eight
    elif t1c1.click == 9:
        curr = t1c1.nine
    elif t1c1.click == 10:
        curr = t1c1.ten
    elif t1c1.click == 11:
        curr = t1c1.eleven
    elif t1c1.click == 12:
        curr = t1c1.twelve
    else:
        print(error)

#print current click
    print(
        f'{t1c1.name.title()}, click: {t1c1.click}'
        f'\n{t1c1.team1.title()}'
        f'\nrange: {t1c1.rang} targets: {t1c1.bolts}'
        f'\n{t1c1.star}'
        f'\n  movement: {curr[0]}     {curr[4]}'
        f'\n  attack: {curr[1]}      {curr[5]}'
        f'\n  defense: {curr[2]}     {curr[6]}'
        f'\n  damage: {curr[3]}       {curr[7]}'
        '\n\n'
        )

    print(f'last action: {action}')
    action = input('action: ')
    if action == 'end':
        break
                ### use a break statment here to exit loop? ###
                ### also sdd a help print for a list of viable commands ###
    else:
        target = input('target: ')
    if target.lower() in team:
        if action.lower() == 'attack':
            damage = input('damage: ')
            t1c1.click = t1c1.click + int(damage)
            action = f'{action.title()} {target.title()}'
        elif action.lower() == 'heal':
            t1c1.click = int(t1c1.click) - 1
            action = f'{action.title()} {target.title()}'
        else:
            action = 'action neither attack nor heal'
    elif action != 'end':
        action = 'target not on team'
    clear()


input('end of program. \ngoodbye cruel world!')

























