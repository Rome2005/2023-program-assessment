from tkinter import *

class QuizGUI:
    def __init__(self, root):
        # Common format for all buttons
        button_font = ("Arial", 10, "bold")
        button_fg = "#FFFFFF"

        # Quiz GUI Frame
        self.quiz_frame = Frame(root, padx=10, pady=10)
        self.quiz_frame.grid()

        # Row 0: Question box
        self.question_box = Label(self.quiz_frame,
                                  text="Question goes here",
                                  font=("Arial", 12))
        self.question_box.grid(row=0, column=0, columnspan=2, pady=10)

        # Row 1: Answer box
        self.answer_box = Entry(self.quiz_frame,
                                font=("Arial", 12),
                                width=15)
        self.answer_box.grid(row=1, column=0, columnspan=2, pady=10)
        self.answer_box.focus()  # Set focus to answer box when the GUI is opened

        # Row 2: Error message (displayed when the user types something other than a number or nothing)
        self.error_message = Label(self.quiz_frame,
                                   text="",
                                   font=("Arial", 10),
                                   fg="red")
        self.error_message.grid(row=2, column=0, columnspan=2, pady=5)

        # Row 3: Submit and Skip buttons
        self.submit_button = Button(self.quiz_frame,
                                    text="Submit",
                                    bg="#009900",
                                    fg=button_fg,
                                    font=button_font,
                                    width=5,
                                    pady=6,
                                    bd=3,
                                    command=self.submit_answer)
        self.submit_button.grid(row=3, column=0, padx=5, pady=5)

        self.skip_button = Button(self.quiz_frame,
                                  text="Skip",
                                  bg="#CC0000",
                                  fg=button_fg,
                                  font=button_font,
                                  width=5,
                                  pady=6,
                                  bd=3,
                                  command=self.skip_question)
        self.skip_button.grid(row=3, column=1, padx=5, pady=5)

    def submit_answer(self):
        # Replace this method with the actual functionality to process the user's answer
        pass

    def skip_question(self):
        # Replace this method with the actual functionality to skip to the next question
        pass

# Note: Functionality for processing answers and handling skipping to the next question
# needs to be implemented in the `submit_answer` and `skip_question` methods.
