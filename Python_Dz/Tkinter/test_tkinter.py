from tkinter import *

root = Tk()

def FuckYou(click):
    print('Fuck you! leather head')

root.title('test')
root.geometry('600x400')

but1 = Button(root)
but1['text'] = 'Enter'
but1['width'] = 20
but1['height'] = 10
but1.bind('<Button-1>', FuckYou)
but1.pack()



input()