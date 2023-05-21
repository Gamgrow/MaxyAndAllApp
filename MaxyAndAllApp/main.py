
from tkinter.scrolledtext import *
from tkinter.font import Font
from tkinter.messagebox import *
from tkinter.filedialog import *
import speech_recognition as sr
from Maxy_version_1 import doooo
from tkinter import *
import pyttsx3 as pt
import os
import sys
from tkinter import *
wind = Tk()
from Maxy_version_1  import doooo
from PIL import ImageTk, Image
# create date today
wind = Tk()


def command2():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print('listening...')

        r.pause_threshold = 5
        audio = r.listen(mic, timeout=45)

    try:
        print('recognizing...')
        text = r.recognize_google(audio)
        text = text.lower()
    except Exception as e:
        print(e)
        return text
    return text

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

    

if __name__ == '__main__':
    def karo():
            
            
            pt.speak("Listening start")
        # while(True):
            text = command2()
            if text in ["exit", "quit", "stop"]:
                exit()
            else:
                
                doooo(text)

    def func():
        x = var.get().lower()
        doooo(x)


    # for image not error when you convert py to exe
    

    # for title
    wind.title("Maxy")

#  for icon
    path1 = resource_path("mic.png")
    imj = PhotoImage(file=path1)
    wind.iconphoto(False, imj)

    # // window size

    wind.maxsize(width=1480, height=990)
    wind.minsize(width=1480, height=990)
    # wind.geometry("2000x2000")
    wind.colormapwindows()
   
    wind.config(background='#108cff')
    # label 1
    mylabel = Label(wind,font=("arial",20),bg='#108cff',fg='white',justify="left" ,border=1)
    mylabel.place(x=30,y=125)
    # show image
    path2 = resource_path("mic.png")
    my_pic5 = Image.open(path2)

    resize_pic5 = my_pic5.resize((100,102
                                  ), Image.ANTIALIAS)
    new_pic5 = ImageTk.PhotoImage(resize_pic5)
    
    lbl=Label(wind,bg="#108cff").place(x=290,y=60)
    
    # label 2
    mylabel2 = Label(wind,font=("arial",16 ),bg="#108cff",justify="left"   )
    mylabel2.place(x=1000,y=85)



    path3 = resource_path("searchicon.png")
    my_pic = Image.open(path3)


    resize_pic = my_pic.resize((53, 54), Image.ANTIALIAS)
    new_pic = ImageTk.PhotoImage(resize_pic)

    
    # wlcome to maxy
    path4 = resource_path("wctm.png")

    my_pic_wctm = Image.open(path4)

    resize_pic_wctm = my_pic_wctm.resize((388, 124), Image.ANTIALIAS)
    my_pic_wctm = ImageTk.PhotoImage(resize_pic_wctm)
    mylabel2wctm = Label(wind, image=my_pic_wctm,bg="#108cff" , )
    mylabel2wctm.pack(pady=0)

    def about():
        pass
    # menu bar
    menuBar= Menu(wind)
    wind.config(menu=menuBar)

    file_manu = Menu(menuBar)
    menuBar.add_cascade(label="About",menu=file_manu,activeforeground="#108cff",activebackground="#108cff")
    file_manu.add_cascade(label="Made by \n Lalit Max",command=about)
    


    var = StringVar()
    ent = Entry(wind, width=40, font=("Arial", 23), textvariable=var)
    ent.place(x=185, y=780)

    btn = Button(wind, image=new_pic, command=func,activebackground="#108cff",border=2,bg="white")
    btn.place(x=1219 ,y=780)

    btn2 = Button(wind, image=new_pic5, command=karo,activebackground="#108cff",bg="#108cff",border=2).place(x=690,y=610)
    
    wind.mainloop()
