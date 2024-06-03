import tkinter as tk

LIGHT_GRAY = '#F5F5F5'
LABEL_COLOR = '#25265E'
SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
WHITE = '#FFFFFF'
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)
OFF_WHITE = '#F8FAFF'
LIGHT_BLUE = '#CCEDFF'

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("450x667")  # Adjusted width to accommodate the extra column
        self.window.resizable(0, 0)  # To avoid auto resizing
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()  # Function to create frame for display
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "÷", "*": "×", "-": "-", "+": "+"}  # Operator functions
        self.button_frame = self.create_buttons_frame()  # Function to create frame for buttons
        self.button_frame.rowconfigure(0,weight=1)#next line explanation same..

        for x in range(1,5):#helps rows and columns to expand and fit in the screen 
            self.button_frame.rowconfigure(x,weight=1)
            self.button_frame.columnconfigure(x,weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    #the next three functions are to make the buttons functional/press
    
    def add_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()

    
    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_total_label()
        self.update_label()


    def create_clear_button(self):
        button = tk.Button(self.button_frame, text="C", bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0,command=self.clear)
        button.grid(row=0, column=3, columnspan=1, sticky=tk.NSEW)

    def append_operator(self, operator):#this function is to append the operator symbol with the digit when the operator symbol is pressed. eg 9+ etc
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()


    def create_operator_buttons(self):
        for i, (operator, symbol) in enumerate(self.operations.items()):
            row = i
            column = 4  # Pushing operators to the new column on the right side
            button = tk.Button(self.button_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR,
                               font=DEFAULT_FONT_STYLE, borderwidth=0,command=lambda x=operator:self.append_operator(x))
            button.grid(row=row, column=column, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_label()
        self.current_expression=str(eval(self.total_expression))
        self.total_expression=""
        self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                           borderwidth=0,command=self.evaluate)
        button.grid(row=4, column=3, columnspan=1, sticky=tk.NSEW)

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                               font=DIGITS_FONT_STYLE, borderwidth=0,command=lambda x=digit:self.add_to_expression(x))#this line helps for the number to press and then value is shown pn the screen
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def run(self):
        self.window.mainloop()

# Next three lines of code will run only when the script is run through the terminal
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
