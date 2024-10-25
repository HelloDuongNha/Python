from tkinter import *
from tkinter.ttk import *

import googlesearch  # for accessing Google search


def google_search(event=None):
    query = query_txt.get()
    search_results = []
    for search_result in googlesearch.search(query, stop=5, num=1, pause=2):
        print(search_result)
        search_results.append(search_result)


window = Tk()
window.geometry("520x430")
window.title("Web inSite")

row_counter = 0

lbl = Label(window, text="Search", font=("Arial Bold", 16))
lbl.grid(column=0, row=row_counter, columnspan=3, sticky="W")

row_counter += 1

lbl = Label(window, text="Query:", font=("Arial Bold", 10))
lbl.grid(column=0, row=row_counter, sticky="E", padx=5, pady=5)

query_txt = Entry(window, width=65)
query_txt.bind('<Return>', google_search)
query_txt.grid(column=1, columnspan=6, row=row_counter, sticky="W", padx=5, pady=5)

window.mainloop()
