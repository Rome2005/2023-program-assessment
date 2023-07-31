from tkinter import *

class MultiplicationGUI:
    def __init__(self, root):
        # Common format for all buttons
        # Arial size 10, with white text
        button_font = ("Arial", 10, "bold")
        button_fg = "#FFFFFF"

        # Smaller padding for buttons
        button_padx = 5
        button_pady = 5

        # Multiplication GUI Frame
        self.multiplication_frame = Frame(root, padx=5, pady=10)
        self.multiplication_frame.grid()

        self.multiplication_heading = Label(self.multiplication_frame, 
                                            text="Multiplication",
                                            font=("Arial", 14, "bold"))
        self.multiplication_heading.grid(row=0, column=0, columnspan=6)

        instructions = "Test your multiplication skills here!"
        self.multiplication_text = Label(self.multiplication_frame, 
                                         text=instructions,
                                         wrap=150,
                                         width=30,
                                         pady=6,
                                         justify="left")
        self.multiplication_text.grid(row=1, column=0, columnspan=6)

        instructions = "Select desired tables below"
        self.multiplication_instructions = Label(self.multiplication_frame, 
                                                 text=instructions,
                                                 wrap=150,
                                                 width=30,
                                                 pady=6,
                                                 justify="left")
        self.multiplication_instructions.grid(row=2, column=0, columnspan=6)
      
        # Times Tables buttons
        self.selected_times_table = IntVar()
        self.times_table_buttons = []
        for i in range(1, 13):
            row_index = (i - 1) // 6 + 3
            col_index = (i - 1) % 6
            button = Button(self.multiplication_frame,
                            text=str(i),
                            font=button_font,
                            fg=button_fg,
                            bg="#3399FF",
                            bd=3,
                            command=lambda num=i: self.select_times_table(num),
                            padx=button_padx,
                            pady=button_pady,
                            relief="raised")
            button.grid(row=row_index, column=col_index, padx=5, pady=5)
            self.times_table_buttons.append(button)

        # Configure row and column options for even distribution of extra space
        for i in range(3, 5):
            self.multiplication_frame.grid_rowconfigure(i, weight=1)
        for i in range(6):
            self.multiplication_frame.grid_columnconfigure(i, weight=1)

        self.result_label = Label(self.multiplication_frame, text="", font=button_font)
        self.result_label.grid(row=5, column=0, columnspan=6, padx=5, pady=5)

        # Difficulty buttons
        self.selected_difficulty = IntVar()
        self.difficulty_button_frame = Frame(self.multiplication_frame)
        self.difficulty_button_frame.grid(row=6, column=0, columnspan=6)

        # Easy button
        self.easy_button = Button(self.difficulty_button_frame,
                                  text="Easy",
                                  bg="#009900",
                                  fg=button_fg,
                                  font=button_font,
                                  width=12,
                                  pady=6,
                                  bd=3,
                                  command=lambda: self.select_difficulty(1),
                                  relief="raised")
        self.easy_button.grid(row=0, column=0, padx=5, pady=5)

        # Medium button
        self.medium_button = Button(self.difficulty_button_frame,
                                    text="Medium",
                                    bg="#FF8000",
                                    fg=button_fg,
                                    font=button_font,
                                    width=12,
                                    pady=6,
                                    bd=3,
                                    command=lambda: self.select_difficulty(2),
                                    relief="raised")
        self.medium_button.grid(row=0, column=1, padx=5, pady=5)

        # Hard button
        self.hard_button = Button(self.difficulty_button_frame,
                                  text="Hard",
                                  bg="#CC0000",
                                  fg=button_fg,
                                  font=button_font,
                                  width=12,
                                  pady=6,
                                  bd=3,
                                  command=lambda: self.select_difficulty(3),
                                  relief="raised")
        self.hard_button.grid(row=0, column=2, padx=5, pady=5)

        # Start button
        self.start_button_frame = Frame(self.multiplication_frame)
        self.start_button_frame.grid(row=7, column=0, columnspan=6)

        self.start_button = Button(self.start_button_frame,
                                  text="Start",
                                  bg="#7F00FF",
                                  fg=button_fg,
                                  font=button_font,
                                  width=12,
                                  pady=6,
                                  bd=3)
        self.start_button.grid(row=0, column=0, padx=5, pady=5)

    def select_times_table(self, num):
        if self.selected_times_table.get() == num:
            self.selected_times_table.set(0)  # Deselect the button if it's already selected
            self.times_table_buttons[num - 1].config(relief="raised")  # Change relief to "raised"
        else:
            self.selected_times_table.set(num)
            self.times_table_buttons[num - 1].config(relief="sunken")  # Change relief to "sunken"

    def get_selected_times_table(self):
        return self.selected_times_table.get()

    def select_difficulty(self, num):
        if self.selected_difficulty.get() == num:
            self.selected_difficulty.set(0)  # Deselect the button if it's already selected
            self.update_difficulty_buttons()
        else:
            self.selected_difficulty.set(num)
            self.update_difficulty_buttons()

    def update_difficulty_buttons(self):
        difficulties = [self.easy_button, self.medium_button, self.hard_button]
        for i, button in enumerate(difficulties, start=1):
            if i == self.selected_difficulty.get():
                button.config(relief="sunken")
            else:
                button.config(relief="raised")

root = Tk()
root.title("Multiplication Quiz")
gui = MultiplicationGUI(root)
root.mainloop()