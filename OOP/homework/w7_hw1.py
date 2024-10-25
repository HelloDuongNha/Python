from tkinter import *
from tkinter.ttk import *



class MyCombobox:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("350x50")
        self.window.title("GUI Example")

        self.combo = Combobox(self.window)
        self.combo["values"] = ["zero", "one", "two", "three", "four"]
        self.combo.current(1)
        self.combo.grid(column=0, row=0)

        self.btn = Button(self.window, text="Click Me", command=self.clicked)
        self.btn.grid(column=1, row=0)

        self.output = StringVar(self.window)
        self.txt = Entry(self.window, width=30, textvariable=self.output, state="readonly")
        self.txt.grid(column=2, row=0)
    def clicked(self):
        self.res = f"You have selected {self.combo.get()}"
        self.output.set(self.res)
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    win = MyCombobox()
    win.run()