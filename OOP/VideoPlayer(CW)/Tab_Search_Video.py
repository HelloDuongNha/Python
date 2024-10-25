import tkinter as tk
import csv
from Controling_Video_Library import vid 
from tkinter import ttk, messagebox

class SearchVideos:
    def __init__(self, frame):
        self.frame = frame

        self.search_video_lbl = tk.Label(frame, text="Search Video by Name/Director: ", font=("Helvetica", 12))
        self.search_video_lbl.grid(row=0, column=0, padx=10, pady=10, sticky="EN")

        self.search_video_entry = tk.Entry(frame, width=24)
        self.search_video_entry.grid(row=0, column=1, columnspan=1, sticky="W")
        self.search_video_entry.focus_set()

        self.search_video_btn = tk.Button(frame, text="Search", width=12, command=self.search_video)
        self.search_video_btn.grid(row=0, column=2, padx=5, pady=10, sticky="W")

        id = tk.Entry(frame, width=5, state="normal", justify="center")
        id.insert(0, "ID")
        id.place(x=50, y=70)
        id.config(state="readonly")
        self.id_videos_listbox = tk.Listbox(frame, width=5, height=10, selectmode="SINGLE", exportselection=0)
        self.id_videos_listbox.place(x=50, y=100)

        name = tk.Entry(frame, width=20, state="normal", justify="center")
        name.insert(0, "Video's Name")
        name.place(x=115, y=70)
        name.config(state="readonly")
        self.name_videos_listbox = tk.Listbox(frame, width=20, height=10, selectmode="SINGLE", exportselection=0)
        self.name_videos_listbox.place(x=115, y=100)

        director = tk.Entry(frame, width=20, state="normal", justify="center")
        director.insert(0, "Video's Director")
        director.place(x=315, y=70)
        director.config(state="readonly")
        self.director_videos_listbox = tk.Listbox(frame, width=20, height=10, selectmode="SINGLE", exportselection=0)
        self.director_videos_listbox.place(x=315, y=100)

        rate = tk.Entry(frame, width=9, state="normal", justify="center")
        rate.insert(0, "Rating")
        rate.place(x=515, y=70)
        rate.config(state="readonly")
        self.rate_videos_listbox = tk.Listbox(frame, width=9, height=10, selectmode="SINGLE", exportselection=0)
        self.rate_videos_listbox.place(x=515, y=100)

        # Scrollbar
        scrollbar = tk.Scrollbar(frame, orient="vertical", command=self.on_scroll)
        scrollbar.place(x=615, y=100, height=195)

        self.filter_lbl = tk.Label(frame, text="Filter by Director: ", font=("Helvetica", 12))
        self.filter_lbl.place(x=50, y=320)

        self.director_var = tk.StringVar(frame)
        self.director_combobox = ttk.Combobox(frame, textvariable=self.director_var, state="readonly")
        self.director_combobox.place(x=190, y=320)
        self.director_combobox.set("Select a Director")

        self.filter_btn = tk.Button(frame, text="Filter", width=12, command=self.filter_videos)
        self.filter_btn.place(x=400, y=316)
        
        self.refresh_btn = tk.Button(frame, text="Refresh", width=12, command=self.refresh_videos)
        self.refresh_btn.grid(row=0, column=3, padx=10, pady=10, sticky="W")

        # Connect scrollbar to listboxes
        self.id_videos_listbox.config(yscrollcommand=scrollbar.set)
        self.name_videos_listbox.config(yscrollcommand=scrollbar.set)
        self.director_videos_listbox.config(yscrollcommand=scrollbar.set)
        self.rate_videos_listbox.config(yscrollcommand=scrollbar.set)

        # Bind scrolling
        self.id_videos_listbox.bind("<MouseWheel>", self.on_listbox_scroll)
        self.name_videos_listbox.bind("<MouseWheel>", self.on_listbox_scroll)
        self.director_videos_listbox.bind("<MouseWheel>", self.on_listbox_scroll)
        self.rate_videos_listbox.bind("<MouseWheel>", self.on_listbox_scroll)
        
        self.load_videos()

    def on_scroll(self, *args):
        self.id_videos_listbox.yview(*args)
        self.name_videos_listbox.yview(*args)
        self.director_videos_listbox.yview(*args)
        self.rate_videos_listbox.yview(*args)

    def on_listbox_scroll(self, event):
        self.id_videos_listbox.yview('moveto', event.widget.yview()[0])
        self.name_videos_listbox.yview('moveto', event.widget.yview()[0])
        self.director_videos_listbox.yview('moveto', event.widget.yview()[0])
        self.rate_videos_listbox.yview('moveto', event.widget.yview()[0])

    def load_videos(self):
        # Load all videos from CSV to display initially
        try:
            with open(vid.get_library_path(), 'r') as file:
                reader = csv.reader(file)
                self.videos = list(reader)  # Skip the header
            self.update_listbox(self.videos)
            self.update_director_combobox()
        except FileNotFoundError:
            messagebox.showerror("Error", "CSV file not found.")

    def search_video(self):
        input = self.search_video_entry.get().lower().strip()
        if not input: 
            messagebox.showerror("Error", "Please input something to find")
            return
        if not input:
            messagebox.showinfo("Success", "Please enter a search term.")
            self.update_listbox(self.videos)
            return
        results = []
        for video in self.videos:
            video_name_lower = video[1].lower()
            director_name_lower = video[2].lower()
            if input in video_name_lower or input in director_name_lower:
                results.append(video)
        if not results:
            messagebox.showerror("Error", "No results found.")
            self.id_videos_listbox.delete(0, tk.END)
            self.name_videos_listbox.delete(0, tk.END)
            self.director_videos_listbox.delete(0, tk.END)
            self.rate_videos_listbox.delete(0, tk.END)
            return
        self.update_listbox(results)
        messagebox.showinfo("Success", f"Found {len(results)} result(s).")
        self.director_combobox.set("Select a Director")

    def filter_videos(self):
        selected_director = self.director_var.get()
        if selected_director == "Select a Director":
            messagebox.showinfo("Success", "Please select a director.")
            self.update_listbox(self.videos)
            return
        
        results = []
        for video in self.videos:
            if selected_director == video[2]:
                results.append(video)
                self.update_listbox(results)
        messagebox.showinfo("Success", f"Showing videos by {selected_director}.")


    def refresh_videos(self):
        self.load_videos()
        # self.status_lbl.config(text="Video list refreshed.")
        self.director_combobox.set("Select a Director")
        self.search_video_entry.delete(0, tk.END)

    def update_listbox(self, videos):
        self.search_video_entry.focus_set()
        self.id_videos_listbox.config(state="normal")
        self.name_videos_listbox.config(state="normal")
        self.director_videos_listbox.config(state="normal")
        self.rate_videos_listbox.config(state="normal")

        self.id_videos_listbox.delete(0, tk.END)
        self.name_videos_listbox.delete(0, tk.END)
        self.director_videos_listbox.delete(0, tk.END)
        self.rate_videos_listbox.delete(0, tk.END)
        for video in videos:
            self.id_videos_listbox.insert(tk.END, f"   {video[0]:2}.")
            self.name_videos_listbox.insert(tk.END, f"  {video[1]} ")
            self.director_videos_listbox.insert(tk.END, f"  {video[2]} ")
            self.rate_videos_listbox.insert(tk.END, f"  {video[3]} star(s).")
        self.id_videos_listbox.config(state="disable", disabledforeground="black")
        self.name_videos_listbox.config(state="disabled", disabledforeground="black")
        self.director_videos_listbox.config(state="disabled", disabledforeground="black")
        self.rate_videos_listbox.config(state="disabled", disabledforeground="black")

    def update_director_combobox(self):
        directors = sorted(set(video[2] for video in self.videos))
        self.director_combobox['values'] = directors

# if __name__ == "__main__":
#     root = tk.Tk()
#     frame = tk.Frame(root)
#     app = SearchVideos(frame)
#     root.mainloop()
