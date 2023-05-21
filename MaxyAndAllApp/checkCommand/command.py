from tkinter import *
import speech_recognition as sr
import pyttsx3 as pt


def command():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        # print('listening...')

        r.pause_threshold = 5
        audio = r.listen(mic, timeout=45)

    try:
        # print('recognizing...')
        text = r.MaxyBabu(audio, language="en-in")
        text = text.lower()
    except Exception as e:
        printt(e)
        return text
    return text


wind = Tk()

# for title
wind.title("Maxy")


def printt(str):
    mylabel.config(text=str)


def func():
    pt.speak("Listening start")
    str = command()
    printt(str)

# #  for icon
# imj = PhotoImage(file='mic.png')
# wind.iconphoto(False, imj)

# // window size


# wind.maxsize(width=400, height=350)
# wind.minsize(width=400, height=350)
wind.geometry('400x350')

#  for text print

mylabel = Label(wind, text="User Name", bg='red', fg='white',
                width=60, height=5)
mylabel.pack()

btn = Button(wind, text='click me', command=func)
btn.pack()

# mylabel.grid() for left side
# mylabel.place(x=100,y=100)

wind.mainloop()
