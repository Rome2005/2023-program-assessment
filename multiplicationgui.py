from tkinter import *

class MultiplicationGUI:
    def __init__(self, root):
        # common format for all buttons
        # Arial size 12, with white text
        button_font = ("Arial", "12", "bold")
        button_fg = "#FFFFFF"

        # Even padding for buttons
        button_padx = 10
        button_pady = 10

        # Multiplication GUI Frame
        self.multiplication_frame = Frame(root, padx=10, pady=10)
        self.multiplication_frame.grid()

        self.multiplication_heading = Label(self.multiplication_frame, 
                                            text="Multiplication",
                                            font=("Arial", "16", "bold"))
        self.multiplication_heading.grid(row=0, column=0, columnspan=6)

        instructions = "Test your multiplication skills here!"
        self.multiplication_text = Label(self.multiplication_frame, 
                                         text=instructions,
                                         wrap=150,
                                         width=30,
                                         pady=12,
                                         justify="left")
        self.multiplication_text.grid(row=1, column=0, columnspan=6)

        instructions = "Select desired tables below"
        self.multiplication_instructions = Label(self.multiplication_frame, 
                                                 text=instructions,
                                                 wrap=150,
                                                 width=30,
                                                 pady=12,
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

    def select_times_table(self, num):
        if self.selected_times_table.get() == num:
            self.selected_times_table.set(0)  # Deselect the button if it's already selected
            self.times_table_buttons[num - 1].config(relief="raised")  # Change relief to "raised"
        else:
            self.selected_times_table.set(num)
            self.times_table_buttons[num - 1].config(relief="sunken")  # Change relief to "sunken"

    def get_selected_times_table(self):
        return self.selected_times_table.get()
