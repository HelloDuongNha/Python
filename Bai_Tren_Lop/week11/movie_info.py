from tkinter import *
from tkinter.ttk import *

#### 1. CREATE THE WINDOW ####
window = Tk()
window.title("Movie Ticket Info")
window.geometry('300x200')

# movie data
movies = {'Harry Potter': ['Chris Columbus', '2:30', 10.00],
          'The Matrix': ['Lana Wachowski', '2:15', 12.00],
          'The Lord of the Rings': ['Peter Jackson', '3:30', 15.00],
          'The Dark Knight': ['Christopher Nolan', '2:45', 12.00],
          'Inception': ['Christopher Nolan', '2:30', 12.00]}

#### 2. EVENT HANDLERS ####
def cbb_movie_selected(event):
    name = cbb_movie.get()
    movie_info = movies[name]
    director = movie_info[0]
    time = movie_info[1]
    price = movie_info[2]

    set_text(txt_name, name)
    set_text(txt_director, director)
    set_text(txt_time, time)
    set_text(txt_price, price)

def set_text(txt_ui, text):
    txt_ui.configure(state='normal')    # change the state to normal to edit
    txt_ui.delete(0, END)
    txt_ui.insert(0, text)
    txt_ui.configure(state='readonly')  # change the state back to readonly

#### 3. WIDGETS ####
lbl_movie = Label(window, text="Choose a movie:")
lbl_movie.grid(row=0, column=0, sticky=E)

cbb_movie = Combobox(window, width=15, state='readonly')
cbb_movie['values'] = list(movies.keys())
cbb_movie.current(0)
cbb_movie.bind('<<ComboboxSelected>>', cbb_movie_selected)
cbb_movie.grid(row=0, column=1, sticky=W)

lbl_name = Label(window, text="Name:")
lbl_name.grid(row=1, column=0, sticky=E)

txt_name = Entry(window, width=15, state='readonly')
txt_name.grid(row=1, column=1, sticky=W)

lbl_director = Label(window, text="Director:")
lbl_director.grid(row=2, column=0, sticky=E)

txt_director = Entry(window, width=15, state='readonly')
txt_director.grid(row=2, column=1, sticky=W)

lbl_time = Label(window, text="Time:")
lbl_time.grid(row=3, column=0, sticky=E)

txt_time = Entry(window, width=15, state='readonly')
txt_time.grid(row=3, column=1, sticky=W)

lbl_price = Label(window, text="Price:")
lbl_price.grid(row=4, column=0, sticky=E)

txt_price = Entry(window, width=15, state='readonly')
txt_price.grid(row=4, column=1, sticky=W)

#### 4. RUN THE MAIN LOOP ####
window.mainloop()