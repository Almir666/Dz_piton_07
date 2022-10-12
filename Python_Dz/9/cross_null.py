# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP

field = [['_','_','_'],['_','_','_'],['_','_','_']]
players = ['x','0']    
def printField(arr):
    for i in arr:
        for j in i:
            print(j,end="  ")
        print()    
    
# printField(field)

