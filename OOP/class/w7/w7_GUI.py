from tkinter import *

class MyWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry('300x50')
        self.window.title('gui example')

        self.btn = Button(self.window, text="click me", command=self.clicked)
        self.btn.grid(column=0, row=0)
        self.lbl = Label(self.window, text="hello")
        self.lbl.grid(column=1, row=0)

    def clicked(self):
        self.lbl.configure(text="button was clicked")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    win = MyWindow()
    win.run()