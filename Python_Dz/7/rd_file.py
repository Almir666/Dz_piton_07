

def read_file():
    with open('Phone_book_write.txt', 'r') as data:
        l = [line.strip() for line in data]
    print(l)
           
 
read_file()    
