from model_read import f_read
from moder_write import f_write
from find import find
from redact import redact


while True:

    show = int(input('Посмотреть - 1\nДобавить - 2\nПоиск - 3\nРедактировать - 4\nВыход - 0\n'))

    if show == 1:
        print(*f_read(), sep='')
    elif show == 2:
        print(f_write())    
    elif show == 3:
        show_find = int(input('1 - Имя, 2 - Телефон, 3 - должность\n'))
        print(*find(show_find),  sep='')    
    elif show == 4:
        show_red = int(input('1 - Имяб 2 - Телефон, 3 - должность, 4 - пол, 5 - возраст, 6 - зп'))
        redact(show_red)  
    elif show == 0:
        break