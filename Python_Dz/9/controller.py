from isOdd import isOdd
import random

print('Начало игры')

field = [['_','_','_'],['_','_','_'],['_','_','_']]  
player = ['x', '0']

def printField(arr):
    for i in arr:
        for j in i:
            print(j,end="  ")
        print()  
printField(field)      
  
first = random.randint(0, 1)
if first == 0:
        player = '0'
else:
    player = 'x'    

show = print(f'Первым ходит игрок выбравший: {player}')

def check_win (arr):
    flag = False
    for i in range (0,3):
        if (arr[i][0] == arr[i][1]) & (arr[i][0] == arr[i][2]) & (arr[i][0] != "_"):
            flag = True
            return flag     
        if (arr[0][i] == arr[1][i]) & (arr[0][i] == arr[2][i]) & (arr[0][i] != "_"):
            flag=True
            return flag
    if (arr[0][0] == arr[1][1]) & (arr[0][0] == arr[2][2]) & (arr[0][0] != "_"):
        flag=True
        return flag
    if (arr[0][2] == arr[1][1]) & (arr[0][2] == arr[2][0]) & (arr[0][2] != "_"):
        flag=True
        return flag
    return flag

def x_or_o (input_index):
    if not isOdd(input_index):
        result="X"
    else:
        result="O"

def step_player(player, arr):
    flag = False
    while not flag:
        step_p = input('Введите позицию для хода по вертикали и горизонтали от 1 до 3: ')
        step = step_p.split()
        if (arr[int(step[0])-1][int(step[1])-1] == "_"):
            flag = True
            arr[int(step[0])-1][int(step[1])-1] = player
        else:
            print("Данный ход не возможен")
