from tkinter import *

class MyWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("300x50")
        self.window.title("gui example")

        self.input_txt = Entry(self.window, width=10, )
        self.input_txt.focus()
        self.input_txt.grid(column=0, row=0)

        self.btn = Button(self.window, text="click me", command=self.clicked)
        self.btn.grid(column=1, row=0)

        self.output = StringVar(self.window)
        # create Entry object, bind output Stringvar to it
        self.txt = Entry(self.window, width=30, textvariable=self.output, state='readonly')
        self.txt.grid(column=2, row=0)

    def clicked(self):
        res = 'hello ' + self.input_txt.get()   # get text from input_txt Entry
        self.output.set(res)                    

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    win = MyWindow()
    win.run()