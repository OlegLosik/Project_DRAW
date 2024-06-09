import random
total_num = int(input()) #общее число команд
teams = [] #наименования всех команд в списке
while total_num > 0: #добавляем команды в список
    team = input()
    teams.append(team)
    total_num -= 1
random.shuffle(teams) #мешаем команды в списке
dot = 0
pairs = [] #список с парами
def sport(): #составляем пары в списке
    pairs.append(teams[dot])
    pairs.append(':')
    pairs.append(teams[dot + 1])
    teams.pop(0)
    teams.pop(0)
while len(teams) > 0:
    sport()
pairs_tog = []
def sports(): #объединяем пары в списке
    ben = pairs[0] + pairs[1] + pairs[2]
    pairs_tog.append(ben)
    pairs.pop(0)
    pairs.pop(0)
    pairs.pop(0)
while len(pairs) > 0:
    sports()