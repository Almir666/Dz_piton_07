def f_write():
    with open('data.txt', 'a') as data:
        data.write(input('Введите имя, телефон, должность, пол(м\ж), возраст, з\п сотрудника через пробел: ') + '\n')
        return 'запись выполнена\n'