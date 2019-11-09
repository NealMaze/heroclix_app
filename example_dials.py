# call fordial defs 
import dial_def

# example dials
    #Batman Beyond
dkr_01 = [
    '8', '10', '17', '3', 'Leap/Climb',
          'Summon the Bats', 'Toughness', 'Outwit',
    ]
dkr_02 = [
    '8', '11', '17', '2', 'Leap/Climb',
          'Summon the Bats', 'Toughness', 'Outwit',
    ]
dkr_03 = [
    '8', '11', '17', '3', 'Leap/Climb',
          'Summon the Bats', 'Invulnerability', 'Outwit',
    ]
dkr_04 = [
    '6', '11', '17', '2', 'Leap/Climb',
          'Summon the Bats', 'Invulnerability', 'Close Combat Expert',
    ]
dkr_05 = [
    '6', '10', '16', '1', 'Leap/Climb',
          '', 'Invulnerability', 'Close Combat Expert',
    ]
dkr_06 = [
    '6', '10', '16', '2', 'Leap/Climb',
          '', 'Toughness', 'Close Combat Expert',
    ]
dkr_07 = [
    '6', '9', '16', '2', 'Leap/Climb',
          '', 'Toughness', 'Outwit',
    ]
dkr_08 = [
    '6', '9', '16', '1', 'Leap/Climb',
          '', 'Toughness', 'Outwit',
    ]
dkr_09 = ['ko', 'ko', 'ko', 'ko']
dkr_10 = ['ko', 'ko', 'ko', 'ko']
dkr_11 = ['ko', 'ko', 'ko', 'ko']
dkr_12 = ['ko', 'ko', 'ko', 'ko']
batman = dial_def.dial('batman', 140, 1, 'batfamily', 6, 1,
              'Batman can use the Charge \n and the Flight abilities',
              dkr_01, dkr_02, dkr_03, dkr_04, dkr_05, dkr_06, dkr_07, dkr_08,
              dkr_09, dkr_10, dkr_11, dkr_12)

#Batgirl
batgirl_1 = ["9, 10, 17, 3"]
batgirl_2 = ["9, 9, 16, 3"]
batgirl_3 = ["8, 9, 17, 1"]
batgirl_4 = ["8, 10, 18, 2"]
batgirl_5 = ["7, 10, 17, 2"]
batgirl_6 = ["7, 9, 16, 1"]

    #Red Hood
redhood_1 = ["10, 11, 17, 3"]
redhood_2 = ["9, 11, 18, 3"]
redhood_3 = ["8, 10, 16, 3"]
redhood_4 = ["8, 10, 16, 2"]
redhood_5 = ["8, 9, 16, 2"]
redhood_6 = ["7, 8, 16, 1"]
redhood_7 = ["7, 9, 15, 2"]

    #Nightwing
nightwing_1 = ["8, 11, 17, 3"]
nightwing_2 = ["7, 10, 16, 2"]
nightwing_3 = ["7, 9, 17, 2"]
nightwing_4 = ["7, 10, 16, 3"]
nightwing_5 = ["7, 10, 16, 2"]
nightwing_6 = ["6, 9, 17, 2"]

    #Damian Wayne
robin_1 = ["8, 10, 16, 2"]
robin_2 = ["9, 9, 16, 2"]
robin_3 = ["9, 9, 16, 2"]
robin_4 = ["9, 10, 16, 1"]
robin_5 = ["9, 9, 16, 2"]
robin_6 = ["8, 11, 17, 1"]

#player teams stored as lists
p1team = []
p2team = []
p3team = []
p4team = []

current = (dkr029ck1 + "\n" + dkr029ck4)
print (current)

























