
from tkinter import *
from tkinter import colorchooser
curr_x, curr_y = 0, 0

def locate_xy(event):
    global curr_x, curr_y
    curr_x, curr_y = event.x, event.y
    print(curr_x, curr_y)


def addline(event):
    global curr_x, curr_y
    c.create_line((curr_x, curr_y, event.x, event.y), fill=color, width=3)
    curr_x, curr_y = event.x, event.y

def pen_color():
    global color
    color = colorchooser.askcolor()[1]


root = Tk()
root.title('Paint')
root.geometry('500x400')
root.resizable(False, False)

menu_bar = Menu(root)
options = Menu(menu_bar, tearoff=0)
options.add_command(label='Color', command=pen_color)
options.add_separator()
options.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='Options', menu=options)
root.config(menu=menu_bar)

c = Canvas(root, width=500, height=400)
c.pack()
c.bind('<Button-1>', locate_xy)
c.bind('<B1-Motion>', addline)


root.mainloop()
