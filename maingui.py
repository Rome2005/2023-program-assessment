from tkinter import *
from multiplicationgui import MultiplicationGUI

class MainGUI:
    def __init__(self, root):
        # common format for all buttons
        # Arial size 14, with white text
        button_font = ("Arial", "14", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.main_frame = Frame(root, padx=10, pady=10)
        self.main_frame.grid()

        self.main_heading = Label(self.main_frame,
                                  text="Math Quiz",
                                  font=("Arial", "16", "bold"))
        self.main_heading.grid(row=0)

        instructions = "Pick a math operation!"
        self.main_instructions = Label(self.main_frame,
                                       text=instructions,
                                       wrap=150,
                                       width=30,
                                       pady=12,
                                       justify="left")
        self.main_instructions.grid(row=1)

        # Operation buttons
        self.button_frame = Frame(self.main_frame)
        self.button_frame.grid(row=2)

        # Addition +
        self.addition_button = Button(self.button_frame,
                                      text="Addition +",
                                      bg="#009900",
                                      fg=button_fg,
                                      font=button_font,
                                      width=12,
                                      pady=10,
                                      bd=3,
                                      command=self.open_addition_gui)
        self.addition_button.grid(row=0, column=0, padx=5, pady=5)

        # Subtraction -
        self.subtraction_button = Button(self.button_frame,
                                         text="Subtraction -",
                                         bg="#1231FF",
                                         fg=button_fg,
                                         font=button_font,
                                         width=12,
                                         pady=10,
                                         bd=3)
        self.subtraction_button.grid(row=0, column=1, padx=5, pady=5)

        # Multiplication ×
        self.multiplication_button = Button(self.button_frame,
                                            text="Multiplication ×",
                                            bg="#CC0000",
                                            fg=button_fg,
                                            font=button_font,
                                            width=12,
                                            pady=10,
                                            bd=3,
                                            command=self.open_multiplication_gui)
        self.multiplication_button.grid(row=1, column=0, padx=5, pady=5)

        # Division ÷
        self.division_button = Button(self.button_frame,
                                      text="Division ÷",
                                      bg="#CC6600",
                                      fg=button_fg,
                                      font=button_font,
                                      width=12,
                                      pady=10,
                                      bd=3)
        self.division_button.grid(row=1, column=1, padx=5, pady=5)

    def open_addition_gui(self):
        # Create a new window for the Addition GUI
        # Implement your Addition GUI code here
        pass

    def open_multiplication_gui(self):
        # Create a new window for the Multiplication GUI
        multiplication_window = Toplevel()
        multiplication_window.title("Multiplication GUI")
        multiplication_gui = MultiplicationGUI(multiplication_window)

  
# Note: The open_addition_gui method is left empty for you to add the Addition GUI code.
# You can create another file "additiongui.py" and follow a similar structure to create
# the Addition GUI class and import it into this "main.py".