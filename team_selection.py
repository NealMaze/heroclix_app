# Eric,I just want to check the name : value of each class in a list, and for
# every positive, print 'one dial found'

#temp dial def
class dial:
    def __init__(
    self,
    name,
    point,
    ):
        self.name = name
        self.point = point

#temp dials
b029 = dial('batman', 140)
a203 = dial('captain america', 90)
b002 = dial('batgirl', 67)
r023 = dial('red hood', 125)
i009 = dial('iron man', 225)
b058 = dial('batman', 152)
n007 = dial('nightwing', 94)
t200 = dial('thor', 250)
r042 = dial('robin', 43)

# temp list characters not chosen
unselected_chars = [b029, a203, b002, r023, i009, b058, n007, t200, r042]

select_char = 'none'

# ask how many teams (not implemented yet)
num_of_teams = input('How many teams: ')

# ask team point limit (not implemented yet)
point_limit = input('How many points per team: ')

while select_char != 'done':
    select_char = input('Character Selection: ')
    for character in unselected_chars:
        if character.name == select_char:
            print(f'{character.name}\n{character.point}')

        

# (later) alternate between teams selecting teams
# add together and check team values vs limit
# if a player reaches team limit or opts out,:
    # continue drafting while skipping finnished players











