# python3.7
import re
import csv

def fuck(dial, value, location):
    if len(dial) > (location):
        if dial[location] != value:
            dial.insert(location, f'{value}_null')
            dial.insert(location, f'{value}_null')
            dial.insert(location, f'{value}_null')
    elif len(dial) == location:
        dial.append(f'{value}_null')
        dial.append(f'{value}_null')
        dial.append(f'{value}_null')
    elif len(dial) < location:
        dial.append(f'{value}_null')
        dial.append(f'{value}_null')
        dial.append(f'{value}_null')
    else:
        print([dial[0], dial[0], dial[0], dial[0], dial[0], dial[0], dial[0], dial[0]])

def put(list, value, location):
    for dial in list:
        if len(dial) > location:
            if dial[location] != value:
                dial.insert(location, f'{value}_null')
            location = location + 1
            if dial[location] != value:
                dial.insert(location, f'{value}_null')
            location = location + 1
            if dial[location] != value:
                dial.insert(location, f'{value}_null')
            location = location - 2

def put2(list, value, location):
    for dial in list:
        fuck(dial, value, location)
        location = location + 3
        fuck(dial, value, location)
        location = location + 3
        fuck(dial, value, location)
        location = location - 6


def put3(list, value, location):
    for dial in list:
        if len(dial) > location:
            if dial[location] != value:
                dial.insert(location, f'{value}_null')
                dial.insert(location, f'{value}_null')
                dial.insert(location, f'{value}_null')
        elif len(dial) == location:
            dial.append(f'{value}_null')
            dial.append(f'{value}_null')
            dial.append(f'{value}_null')
        elif len(dial) < location:
            dial.append(f'{value}_null')
            dial.append(f'{value}_null')
            dial.append(f'{value}_null')
        else:
            print([dial[0], dial[0], dial[0], dial[0], dial[0], dial[0], dial[0], dial[0]])


ofile = open('dials_1.1.txt', 'r')
nfile = ofile.read()
zfile = nfile.replace(';', ':')
file = zfile.replace('|', ', ')

# split each dial into a separate entry in list
odials = file.split('\n\n')

dials = []
for odial in odials:
    dial = re.split('\[|\]|\(|\)| R | U | V | E | LE | :|:\[|slot=', odial)
    stripped_dial = [value.strip() for value in dial]
    dials.append(stripped_dial)

blacklist = ['Team:', 'Range:', 'click', 'Keywords:',
             'b', '/b', 'Points:', '', ' ', 'header', 'icon',
             '/icon', 'dial', '/dial', '/header', '/slot', '/click',
             ]

# Filter out the elements that are in the blacklist
dials = [[val for val in dial if val not in blacklist] for dial in dials]

ldials = []
y = 0
for dial in dials:
    if dial[0] == 'dofpG002e':
        dials.remove(dial)
        ldials.append(dial)
y = 0
for dial in dials:
    if dial[0] == 'wkDP17-001':
        dials.remove(dial)
        ldials.append(dial)
for dial in dials:
    if len(dial) > 140:
        dials.remove(dial)
        ldials.append(dial)



put3(dials, 'Improved', 107)
put2(dials, 'Special', 110)
for dial in dials:
    fuck(dial, 'Speed', 119)
for dial in dials:
    fuck(dial, 'Attack', 122)
for dial in dials:
    fuck(dial, 'Defense', 125)
for dial in dials:
    fuck(dial, 'Damage', 128)

put2(ldials, 'Special', 171)
for dial in ldials:
    fuck(dial, 'Speed', 180)
for dial in ldials:
    fuck(dial, 'Attack', 183)
for dial in ldials:
    fuck(dial, 'Defense', 186)
for dial in ldials:
    fuck(dial, 'Damage', 189)

for dial in dials:
    dial.append('Damage_null')

for dial in dials:
    if dial[128] == 'Damage' or 'Damage_null':
        dial.remove(dial[128])
    if dial[125] == 'Defense' or 'Defense_null':
        dial.remove(dial[125])
    if dial[122] == 'Attack' or 'Attack_null':
        dial.remove(dial[122])
    if dial[119] == 'Speed' or 'Speed_null':
        dial.remove(dial[119])
    if dial[116] == 'Special' or 'Special_null':
        dial.remove(dial[116])
    if dial[113] == 'Special' or 'Special_null':
        dial.remove(dial[113])
    if dial[110] == 'Special' or 'Special_null':
        dial.remove(dial[110])
    if dial[107] == 'Improved' or 'Improved_null':
        dial.remove(dial[107])

######################################################################################################################

def luk(ser):
    y = 0
    for dial in dials:
        if dial[0] == ser:
            for value in dial:
                print(y)
                print(value)
                print('\n')
                y = y + 1
            print('item count:')
            print(len(dial))

def luk2(ser, ser2):
    y = 0
    for dial in dials:
        if dial[0] == ser:
            one = dial
    for dial in dials:
        if dial[0] == ser2:
            two = dial
    for value in dial:
        print(y)
        print(one[y])
        print(two[y])
        print('\n')
        y = y + 1
    print(len(one))
    print(len(two))


def chek(pos, valu, suc):
    suc = 0
    x = [valu, f'{valu}_null']
    for dial in dials:
        if dial[pos] not in x:
            print(dial[0])
            print(valu)
        else:
            suc = suc + 1
    print(valu)
    print(suc)

def save_csv(csvname):
    csvfile = open(csvname, 'w')
    writer = csv.writer(csvfile, delimiter = '|', lineterminator = '\n')
    for dial in dials:
        writer.writerow(dial[0:-1])

###################################################################################################################################

ts = 0
print('too small:')
for dial in dials:
    if len(dial) < 124:
        ts = ts + 1
        print(dial[0])
print(ts)


print('too big:')
tb = 0
for dial in dials:
    if len(dial) > 124:
        tb = tb + 1
print(tb)
luk('slosh039')

