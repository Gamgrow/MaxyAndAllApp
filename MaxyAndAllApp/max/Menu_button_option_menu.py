
from tkinter import *
from tkinter import ttk


wind = Tk()


# for title
wind.title("Maxy")

#  for icon
# imj = PhotoImage(file="C:\\Users\\lalit\\OneDrive\\Desktop\\max\\mic.png")
# wind.iconphoto(False, imj)

# // window size

# wind.maxsize(width=400, height=350)
# wind.minsize(width=400, height=350)
wind.geometry('400x350')

def demo():
    pass
def demo2():
    pass
def demo3():
    pass
#  menu bar
menuBar= Menu(wind)
wind.config(menu=menuBar)

# entry box
var = StringVar()
ent = Entry(wind, bg='orange', fg="black", bd=2, font=('Arial'), textvariable=var)
ent.place(x=120, y=30)

# file

file_manu = Menu(menuBar)
menuBar.add_cascade(label="File",menu=file_manu)
file_manu.add_cascade(label="new",command=demo)
file_manu.add_separator()
file_manu.add_cascade(label="papa",command=demo)

# edit
edit_menu = Menu(menuBar)
menuBar.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_cascade(label="Undo",command=demo2)

# view
view = Menu(menuBar)
menuBar.add_cascade(label="view",menu=view)
view.add_cascade(label="hello",menu=demo3)
wind.mainloop()
 