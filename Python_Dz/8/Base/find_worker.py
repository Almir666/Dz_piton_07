# find = str(input())

def read_file():
    with open('data.txt', 'r') as data:
        find_str = []
        l = [line.strip() for line in data]
        for i in l:
            find_str.append(i)
        return print(find_str)    
            # if input == find_str[i]:
            #     print(find_str[i])    
            # else:
            #     print('Такого человека нет в базе')       
read_file()   