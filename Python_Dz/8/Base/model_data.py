value = input('Введите имя, телефон, пол(м\ж), возраст, должность, з\п сотрудника через пробел: ')

def write_name(value):
    with open('data.txt', 'a') as data:
        for i in value:
            data.write(''.join(i))
        data.write('\n')
write_name(value)          