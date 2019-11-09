error = 'what the fuck did you do?'
action = 'none'

# allow program to clear in terminal after every turn 
from os import system, name
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



# example dials
    #Batman Beyond
dkr_01 = ['8', '10', '17', '3', 'Leap/Climb',
          'Summon the Bats', 'Toughness', 'Outwit']
dkr_02 = ['8', '11', '17', '2', 'Leap/Climb',
          'Summon the Bats', 'Toughness', 'Outwit']
dkr_03 = ['8', '11', '17', '3', 'Leap/Climb',
          'Summon the Bats', 'Invulnerability', 'Outwit']
dkr_04 = ['6', '11', '17', '2', 'Leap/Climb',
          'Summon the Bats', 'Invulnerability', 'Close Combat Expert']
dkr_05 = ['6', '10', '16', '1', 'Leap/Climb',
          '', 'Invulnerability', 'Close Combat Expert']
dkr_06 = ['6', '10', '16', '2', 'Leap/Climb',
          '', 'Toughness', 'Close Combat Expert']
dkr_07 = ['6', '9', '16', '2', 'Leap/Climb',
          '', 'Toughness', 'Outwit']
dkr_08 = ['6', '9', '16', '1', 'Leap/Climb',
          '', 'Toughness', 'Outwit']
dkr_09 = ['ko', 'ko', 'ko', 'ko']
dkr_10 = ['ko', 'ko', 'ko', 'ko']
dkr_11 = ['ko', 'ko', 'ko', 'ko']
dkr_12 = ['ko', 'ko', 'ko', 'ko']
batman = dial('batman', 140, 1, 'batfamily', 6, 1,
              'Batman can use the Charge \n and the Flight abilities',
              dkr_01, dkr_02, dkr_03, dkr_04, dkr_05, dkr_06, dkr_07, dkr_08,
              dkr_09, dkr_10, dkr_11, dkr_12)

action = 'none'
t1c1 = batman
team = [t1c1.name]
target = team[0]

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
    if action == 'surrender':
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

























