from tkinter import *
from maingui import MainGUI
from multiplicationgui import MultiplicationGUI
from quizgui import QuizGUI 

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Math Program")
    maingui = MainGUI(root)
    root.mainloop()