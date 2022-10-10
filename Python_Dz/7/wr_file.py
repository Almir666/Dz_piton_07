def write_file(value):
    with open('Phone_book_write.txt', 'a') as data:
        for i in value:
            data.write(''.join(i))
        data.write('\n')
          