from tkinter import *
import random

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

        # Row 1: Question count
        self.question_count_label = Label(self.quiz_frame,
                                          text="",
                                          font=("Arial", 10))
        self.question_count_label.grid(row=1, column=0, columnspan=2, pady=5)

        # Row 2: Answer box
        self.answer_box = Entry(self.quiz_frame,
                                font=("Arial", 12),
                                width=15)
        self.answer_box.grid(row=2, column=0, columnspan=2, pady=10)
        self.answer_box.focus()  # Set focus to answer box when the GUI is opened

        # Row 3: Error message (displayed when the user types something other than a number or nothing)
        self.error_message = Label(self.quiz_frame,
                                   text="",
                                   font=("Arial", 10),
                                   fg="red")
        self.error_message.grid(row=3, column=0, columnspan=2, pady=5)

        # Row 4: Submit, Skip, and Result buttons
        self.submit_button = Button(self.quiz_frame,
                                    text="Submit",
                                    bg="#009900",
                                    fg=button_fg,
                                    font=button_font,
                                    width=8,
                                    pady=6,
                                    bd=3,
                                    command=self.submit_answer)
        self.submit_button.grid(row=4, column=0, padx=5, pady=5)

        self.skip_button = Button(self.quiz_frame,
                                  text="Skip",
                                  bg="#CC0000",
                                  fg=button_fg,
                                  font=button_font,
                                  width=8,
                                  pady=6,
                                  bd=3,
                                  command=self.skip_question)
        self.skip_button.grid(row=4, column=1, padx=5, pady=5)

        self.result_label = Label(self.quiz_frame, text="", font=button_font)
        self.result_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Additional buttons for Retry and Back to Menu
        self.retry_button = Button(self.quiz_frame,
                                   text="Retry",
                                   bg="#7F00FF",
                                   fg=button_fg,
                                   font=button_font,
                                   width=8,
                                   pady=6,
                                   bd=3,
                                   command=self.retry_quiz,
                                   state="disabled")
        self.retry_button.grid(row=6, column=0, padx=5, pady=5)

        self.back_to_menu_button = Button(self.quiz_frame,
                                          text="Back to Menu",
                                          bg="#FF0000",
                                          fg=button_fg,
                                          font=button_font,
                                          width=12,
                                          pady=6,
                                          bd=3,
                                          command=self.back_to_menu,
                                          state="disabled")
        self.back_to_menu_button.grid(row=6, column=1, padx=5, pady=5)

        # Question data
        self.questions = []  # List to store questions (format: (question, answer))
        self.current_question = None
        self.current_index = 0
        self.total_questions = 10  # Total number of questions

        # Generate some easy multiplication questions
        for _ in range(self.total_questions):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            question = f"{num1} x {num2}"
            answer = num1 * num2
            self.questions.append((question, answer))

        # Initialize the first question
        self.current_question = self.questions[self.current_index]
        self.question_box.config(text=self.current_question[0])
        self.update_question_number()

    def submit_answer(self):
        # Get the user's answer from the answer box
        user_answer = self.answer_box.get()

        # Validate the user's answer (check if it's a number)
        if not user_answer.isdigit():
            self.error_message.config(text="Please enter a valid number.")
            return

        # Convert the user's answer to an integer
        user_answer = int(user_answer)

        # Check if the user's answer is correct
        if user_answer == self.current_question[1]:
            self.result_label.config(text="Correct!", fg="green")
            # Clear the answer box when the answer is correct
            self.answer_box.delete(0, END)
        else:
            self.result_label.config(text="Incorrect!", fg="red")

        # Disable the answer box and submit button after answering
        self.answer_box.config(state="disabled")
        self.submit_button.config(state="disabled")

        # Enable the Retry and Back to Menu buttons
        self.retry_button.config(state="normal")
        self.back_to_menu_button.config(state="normal")

        # Proceed to the next question
        self.next_question()

    def skip_question(self):
        # Proceed to the next question
        self.next_question()

    def next_question(self):
        # Move to the next question
        self.current_index += 1

        # If all questions are answered, display a message and disable the Skip button
        if self.current_index >= len(self.questions):
            self.question_box.config(text="Quiz completed!")
            self.answer_box.config(state="disabled")
            self.submit_button.config(state="disabled")
            self.skip_button.config(state="disabled")
            self.result_label.config(text="", fg="black")
        else:
            # Display the next question
            self.current_question = self.questions[self.current_index]
            self.question_box.config(text=self.current_question[0])
            self.answer_box.delete(0, END)
            self.error_message.config(text="")
            # Enable the answer box and submit button for the next question
            self.answer_box.config(state="normal")
            self.submit_button.config(state="normal")
            # Disable the Retry and Back to Menu buttons until the question is answered
            self.retry_button.config(state="disabled")
            self.back_to_menu_button.config(state="disabled")
            self.update_question_number()

    def retry_quiz(self):
        # Reset the quiz to the beginning and enable the Skip button
        self.current_index = 0
        self.current_question = self.questions[self.current_index]
        self.question_box.config(text=self.current_question[0])
        self.answer_box.config(state="normal")
        self.submit_button.config(state="normal")
        self.skip_button.config(state="normal")
        self.result_label.config(text="", fg="black")
        self.retry_button.config(state="disabled")
        self.back_to_menu_button.config(state="disabled")
        self.update_question_number()

    def back_to_menu(self):
        # Implement the functionality to go back to the main menu
        pass

    def update_question_number(self):
        # Update the question number display (e.g., 3/10 Questions)
        question_number = self.current_index + 1
        self.question_count_label.config(text=f"Question {question_number}/{self.total_questions}")

if __name__ == "__main__":
    root = Tk()
    root.title("Multiplication Quiz")
    quiz_gui = QuizGUI(root)
    root.mainloop()
