from tkinter import *
from tkinter import *

root = Tk()
root.geometry('600x500')
root.title('SIGN UP PAGE')
root.config(bg = 'black')
#_________________________
# FUNCTION:
def submit():
    
    user = StringVar()
    passwd = StringVar()
    
    user = e3.get()
    passwd = e5.get()
    
    print(f'Welcome {user} to our services.')
    print(f'This is your {passwd}.')
#-------------------------------------------------------------------------
# LABELS:

l1 = Label(root, text = 'SIGN UP PAGE', font = ('algerian',25,'bold'),
          width = 20, height = 1, bd = 2, relief = 'solid', fg = 'white',
          bg = 'black')
l1.pack()

l2 = Label(root, text = 'FIRST NAME', font = ('algerian',20,'bold'),
          width = 15, height = 1, bd = 2, relief = 'solid', fg = 'skyblue',
          bg = 'black')
l2.place(x = 40, y = 80)

l3 = Label(root, text = 'LAST NAME', font = ('algerian',20,'bold'),
          width = 15, height = 1, bd = 2, relief = 'solid', fg = 'skyblue',
          bg = 'black')
l3.place(x = 40, y = 160)

l4 = Label(root, text = 'USERNAME', font = ('algerian',20,'bold'),
          width = 15, height = 1, bd = 2, relief = 'solid', fg = 'skyblue',
          bg = 'black')
l4.place(x = 40, y = 240)

l5 = Label(root, text = 'PASSWORD', font = ('algerian',20,'bold'),
          width = 15, height = 1, bd = 2, relief = 'solid', fg = 'skyblue',
          bg = 'black')
l5.place(x = 40, y = 320)

l6 = Label(root, text = 'CONFIRM PASSWORD', font = ('algerian',20,'bold'),
          width = 15, height = 1, bd = 2, relief = 'solid', fg = 'skyblue',
          bg = 'black')
l6.place(x = 97, y = 400)

l7 = Label(root, text = 'CONTACT NO', font = ('algerian',20,'bold'),
          width = 15, height = 1, bd = 2, relief = 'solid', fg = 'skyblue',
          bg = 'black')
l7.place(x = 40, y = 480)

l8 = Label(root, text = 'EMAIL', font = ('algerian',20,'bold'),
          width = 15, height = 1, bd = 2, relief = 'solid', fg = 'skyblue',
          bg = 'black')
l8.place(x = 5, y = 560)
#----------------------------------------------------------------------------
# ENTRY:

e1 = Entry(root, width = 30, bg = 'lightgrey')
e1.place(x = 300, y = 84)

e2 = Entry(root, width = 30, bg = 'lightgrey')
e2.place(x = 300, y = 168)

e3 = Entry(root, width = 30, bg = 'lightgrey')
e3.place(x = 300, y = 252)

e4 = Entry(root, width = 30, bg = 'lightgrey', show = "*")
e4.place(x = 300, y = 336)

e5 = Entry(root, width = 30, bg = 'lightgrey', show = "*")
e5.place(x = 400, y = 410)

e6 = Entry(root, width = 30, bg = 'lightgrey')
e6.place(x = 300, y = 490)

e7 = Entry(root, width = 30, bg = 'lightgrey')
e7.place(x = 300, y = 570)

#-------------------------------------------------------------------------
# BUTTON:

b1 = Button(root, text = 'SUBMIT', font = ('algerian', 20, 'bold'),
           fg = 'yellow', bg = 'red', width = 10, height = 1,
           bd = 2, relief = 'solid', activebackground = 'white', command = submit)
b1.place(x = 150, y = 650)
root.mainloop()