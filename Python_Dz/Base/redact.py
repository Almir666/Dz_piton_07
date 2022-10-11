def redact(num):
    list = []
    Vac = {1:'имя', 2:'телефон', 3:'должность', 4:'пол', 5: 'возраст', 6:'зп'}
    Find = input(f'выберите {Vac[num]} для изменения')
    with open('data.txt', 'r') as data:
        x = data.readlines()
        for index, word in enumerate(x):
            if Find in word:
                print(word)
                swap = input('новая запись')
                word = word.split()
                word[num - 1] = swap
                x[index] = ' '.join(word + '\n')
                break
        with open('data.txt', 'w') as data1:        
            data1.writelines(x)        
    print(*x, sep='')            