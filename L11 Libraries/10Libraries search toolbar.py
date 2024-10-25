from tkinter import *
from tkinter.ttk import *

import bs4  # Beautiful Soup - for parsing html content
import googlesearch  # for accessing Google search
import html_text  # for extracting visible text from html content
import requests  # for downloading a web page
import wikipedia  # for accessing Wikipedia pages


def google_search(event=None):
    query = query_txt.get()
    search_results = []
    for search_result in googlesearch.search(query, stop=5, num=1, pause=2):
        print(search_result)
        search_results.append(search_result)
    combo["values"] = search_results
    combo.current(0)
    load_combobox_selection(None)


def load_combobox_selection(event=None):
    url = combo.get()
    load_webpage_text(url)


def wikipedia_lookup():
    query = query_txt.get()
    results = wikipedia.summary(query, sentences=2)
    print(results)


def load_webpage_text(url):
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")
    text = html_text.extract_text(str(soup))
    print(text)


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

row_counter += 1

toolbar = Frame(window)
toolbar.grid(column=1, row=row_counter, columnspan=6)

btn = Button(toolbar, text="Google", command=google_search)
btn.grid(column=0, row=0, padx=5, pady=5)

combo = Combobox(toolbar)
combo.bind("<<ComboboxSelected>>", load_combobox_selection)
combo["values"] = [""]
combo.current(0)
combo.grid(column=1, row=0, padx=5, pady=5)

btn = Button(toolbar, text="Wikipedia", command=wikipedia_lookup)
btn.grid(column=2, row=0, padx=5, pady=5)

window.mainloop()
