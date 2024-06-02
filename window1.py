import tkinter as tk

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")  # Corrected the dimensions
        self.window.resizable(0, 0)  # To avoid auto resizing
        self.window.title("Calculator")

    def run(self):
        self.window.mainloop()

# next three lines of code will run only when the script is run through the terminal
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
