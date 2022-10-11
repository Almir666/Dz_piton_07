def find(num):
    list = []
    Vac = {1:'имя', 2:'телефон', 3:'должность'}
    Find = input(f'выберите {Vac[num]} для поиска')
    with open('data.txt') as data:
        for word in data:
            if Find in word:
                list.append(word)
    return list            