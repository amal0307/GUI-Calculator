import tkinter as tk
LIGHT_GRAY='#F5F5F5'

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")  # Corrected the dimensions
        self.window.resizable(0, 0)  # To avoid auto resizing
        self.window.title("Calculator")

        self.display_frame=self.create_display_frame()
        self.button_frame=self.create_buttons_frame()

    def create_display_frame(self):
        frame=tk.Frame(self.window,height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True,fill="both")
        return frame
    
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both")

    def run(self):
        self.window.mainloop()

# next three lines of code will run only when the script is run through the terminal
if __name__ == "__main__":
    calc = Calculator()
    calc.run()
