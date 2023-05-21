from AppOpener import give_appnames
from AppOpener import open
from AppOpener import features

# a = features.open_things('i vcam')
# print(a)
open("iv cam")


# # # # # s = give_appnames()
# # # # # print(s)


# # # # # def openapp(text):
# # # # #     if text in s:
# # # # #         open(text)


# # # # # openapp('camera')


# # # import tkinter as tk
# # # import AppOpener

# # # # Create the root window
# # # root = tk.Tk()
# # # root.title("AppOpener with Tkinter")

# # # # Set the size and position of the window using the geometry() method
# # # root.geometry("500x500+{}+{}".format(int(root.winfo_screenwidth()/2 - 350), int(root.winfo_screenheight()/2 - 350)))

# # # # Create the text area
# # # text_area = tk.Text(root, height=10, width=30, font=("Helvetica", 20))
# # # text_area.pack()

# # # # Create the button
# # # button = tk.Button(root, text="Submit", font=("Helvetica", 20))
# # # button.pack()

# # # # Create the label
# # # label = tk.Label(root, text="", font=("Helvetica", 20))
# # # label.pack()
# # # text_area.focus()
# # # # Define the function to be called when the button is clicked
# # # def submit(event):
# # #   # Get the text entered in the text area
# # #   text = text_area.get("1.0", "end")
# # #   AppOpener.open(str(text))
# # #   # Set the text of the label to the entered text
# # #   label.config(text=str("Looking for "+text))
# # #   # Clear the text area
# # #   text_area.delete("1.0", "end")

# # # # Bind the submit function to the button's click event
# # # button.bind("<Button-1>", submit)

# # # # Bind the "Return" key to the button's click event
# # # root.bind("<Return>", submit)

# # # # Start the main event loop
# # # root.mainloop()

# # from AppOpener import open, close


# # def main():
# #     print()
# #     print("1. Open <any_name> TO OPEN APPLICATIONS")
# #     print("2. Close <any_name> TO CLOSE APPLICATIONS")
# #     print()
# #     open("help")
# #     print("TRY OPEN <KEY>")
# #     print()
# #     while True:
# #         inp = input("ENTER APPLICATION TO OPEN / CLOSE: ").lower()
# #         if "close " in inp:
# #             app_name = inp.replace("close ", "").strip()
# #             # App will be close be it matches little bit too (Without printing context (like CLOSING <app_name>))
# #             close(app_name, match_closest=True, output=False)
# #         if "open " in inp:
# #             app_name = inp.replace("open ", "")
# #             # App will be open be it matches little bit too
# #             open(app_name, match_closest=True)


# # if __name__ == '__main__':
# #     main()

# from AppOpener import give_appnames, open
# from pyreadline3 import Readline
# readline = Readline()


# class MyCompleter(object):
#     def __init__(self, options):
#         self.options = sorted(options)

#     def complete(self, text, state):
#         if state == 0:
#             if text:
#                 self.matches = [
#                     s for s in self.options if s and s.startswith(text)]
#             else:
#                 self.matches = self.options[:]
#         try:
#             return self.matches[state]
#         except IndexError:
#             return None


# tags = give_appnames()  # FETCH ALL APPNAMES AS DICTIONARY

# completer = MyCompleter(tags)

# readline.set_completer(completer.complete)
# readline.parse_and_bind('tab: complete')

# print("PRESS 'TAB' to autocomplete")

# while True:
#     inp = input("ENTER APPNAME TO OPEN: ")
#     # open(inp)
#     MyCompleter(inp)

# import sys, AppOpener
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextEdit, QVBoxLayout
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import QRect

# class MyApp(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.initUI()

#     def initUI(self):
#         # get the screen dimensions and calculate the center position
#         screen_geometry = QApplication.desktop().screenGeometry()
#         x = (screen_geometry.width() - self.width()) / 2
#         y = (screen_geometry.height() - self.height()) / 2

#         # cast the center coordinates to int and set the window dimensions
#         x = int(x)
#         y = int(y)
#         self.setGeometry(x, y, 500, 500)
#         self.setWindowTitle('AppOpener with Pyqt')

#         # create text area and submit button
#         self.text_area = QTextEdit(self)
#         self.text_area.setFont(QFont('SansSerif', 20))
#         self.submit_btn = QPushButton('Submit', self)
#         self.submit_btn.clicked.connect(self.on_submit)

#         # set the submit button's shortcut to the Return key
#         self.submit_btn.setShortcut('Return')

#         # create label for displaying text
#         self.label = QLabel(self)
#         self.label.setFont(QFont('SansSerif', 20))

#         # use a vertical layout to arrange the text area, submit button, and label
#         layout = QVBoxLayout()
#         layout.addWidget(self.text_area)
#         layout.addWidget(self.submit_btn)
#         layout.addWidget(self.label)
#         self.setLayout(layout)

#         self.show()


#     def on_submit(self):
#         text = self.text_area.toPlainText()
#         AppOpener.open(str(text))
#         self.label.setText(str("Looking for "+text.strip()))
#         self.text_area.clear()
#         self.text_area.setFocus()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())


# import os


# # using getlogin() returning username
# # a=os.path.expanduser('~')
# # print(a)
# print(os.environ.get('USERNAME'))


str = "hello baby how are you what are you doing at this time jnj uj ujnninh"

str = str.split()

tt = ""
cnt = 0
check = 1
for i in str:
    if check == 0:
        i = i.capitalize()
        # print(1)

        check = 1
    tt += i+" "
    cnt += 1
    if (cnt == 4):
        tt += "\n"
        cnt = 0
        check = 0
a = open("NEWS")
print(a)
