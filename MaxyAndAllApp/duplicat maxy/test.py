import tkinter as tk
import tkinter
import speech_recognition as sr
import mahakal
from PIL import Image, ImageTk


#  take command for do anything


class window:

    def __init__(self, master):
        self.img = Image.open('mic.png')
        self.img = self.img.resize((329, 300), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        label = tk.Label(master, image=self.img)
        label.pack(expand=True, fill=tk.BOTH)
        btn = tk.Button(root, text="search",
                        activebackground="#108cff", border=2, bg="white")

        btn.place(x=937, y=710)
        if True:
             mahakal.commandd()


root = tk.Tk()
window = window(root)
# btn = tk.Button(root,text="search", command=commandd,activebackground="#108cff",border=2,bg="white")


root.mainloop()
