from aocd import get_data
lines = get_data().splitlines()

globNum = len(lines)

class Blue(int):
    def __new__(cls, num):
        return super().__new__(cls, num)

class Red(int):
    def __new__(cls, num):
        return super().__new__(cls, num)

class Green(int):
    def __new__(cls, num):
        return super().__new__(cls, num)

map_dict = {
        'red': Red,
        'green': Green,
        'blue': Blue,
        }

col_bound = {
        'red': 12,
        'green': 13,
        'blue': 14,
        }

games = {}

for i in range(1, globNum+1):
    games[i] = []

for i, _ in enumerate(lines):
    lines[i] = lines[i].replace(':','|').replace(';','|').replace(',','|').split('|')
    lines[i] = [el.strip() for el in lines[i]]

for i, line in enumerate(lines, start=1):
    for el in line:
        if line.index(el) == 0:
            continue
        games[i] += [map_dict[el.split()[-1]](el.split()[0])]

sumID = 0
for game in games.keys():
    possible = True
    for i in games[game]:
        if ((isinstance(i, Red) and i > 12) or (isinstance(i, Green) and i > 13) or (isinstance(i, Blue) and i > 14)):
            possible=False
            continue
        else:
            continue
    if possible:
        sumID+=game
        continue

# Part 2 starts from here #

games_red = {}
games_green = {}
games_blue = {}
dict_dict = {
        'red': games_red,
        'green': games_green,
        'blue': games_blue,
        }
breakpoint()
for game in games.keys():
    for col in map_dict.keys():
        for i in sorted(games[game])[::-1]:
            if game in dict_dict[col]:
                break
            else:
                if isinstance(i, map_dict[col]):
                    dict_dict[col][game] = i
                    break
                continue
            continue
        continue
    continue

powers = []

for game in games.keys():
    power = 1
    for col in map_dict.keys():
        power*=dict_dict[col][game]
        continue
    powers.append(power)
    continue

