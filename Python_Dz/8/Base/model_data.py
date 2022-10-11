# value = input('Введите имя, телефон, пол(м\ж), возраст, должность, з\п сотрудника через пробел: ')

def write_data(value):
    with open('data.txt', 'a') as data:
        for i in value:
            data.write(''.join(i))
        data.write('\n')
# write_data(value)          