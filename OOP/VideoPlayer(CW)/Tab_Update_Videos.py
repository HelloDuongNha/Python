import tkinter as tk
import csv
import os
import Tab_Main_GUI as set_text

from tkinter import Listbox, messagebox, filedialog
from Controling_Video_Library import vid
from Controling_List_Library import lis



class UpdateVideos:
    def __init__(self, frame, check_videos_object, create_list_object, search_video_object):
        self.frame = frame

        self.check_video_object = check_videos_object
        self.create_list_object = create_list_object
        self.search_video_object = search_video_object
        # self.recently_deleted_object = recently_deleted_object
        self.video_id = None
        self.video_raw_path = None

        # Create buttons above the left Listbox
        self.view_video_btn = tk.Button(frame, text="List All Videos", command=self.load_videos)
        self.view_video_btn.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.reset_allcount_btn = tk.Button(frame, text="Reset Counting All", width=20, command=self.reset_counting_all)
        self.reset_allcount_btn.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        self.name_lbl = tk.Label(frame, text="Name:", font=("Helvetica", 12))
        self.name_lbl.grid(row=1, column=4, padx=10, pady=10, sticky="E")

        self.name_entry = tk.Entry(frame, width=25)
        self.name_entry.grid(row=1, column=5, columnspan=3,  padx=10, pady=10, sticky="W")
        # self.name_entry.bind("<Return>", self.__add_while_press_Enter)

        self.director_lbl = tk.Label(frame, text="Director:", font=("Helvetica", 12))
        self.director_lbl.grid(row=2, column=4, padx=10, pady=10, sticky="E")

        self.director_entry = tk.Entry(frame, width=25)
        self.director_entry.grid(row=2, column=5, columnspan=3,  padx=10, pady=10, sticky="W")
        # self.director_entry.bind("<Return>", self.__add_while_press_Enter)

        self.rate_lbl = tk.Label(frame, text="Rate:", font=("Helvetica", 12))
        self.rate_lbl.grid(row=3, column=4, padx=10, pady=10, sticky="E")

        self.rate_entry = tk.Entry(frame, width=10)
        self.rate_entry.grid(row=3, column=5, columnspan=2,  padx=10, pady=10, sticky="W")
        tk.Label(frame, text=" stars.").grid(row=3, column=6, sticky="W")

        self.count_lbl = tk.Label(frame, text="Count:", font=("Helvetica", 12))
        self.count_lbl.grid(row=4, column=4, padx=10, pady=10, sticky="E")

        self.count_entry = tk.Entry(frame, width=5)
        self.count_entry.grid(row=4, column=5, columnspan=2, padx=10, pady=10, sticky="W")
        tk.Label(frame, text=" times.").grid(row=4, column=6, sticky="W")

        self.pic_path_lbl = tk.Label(frame, text="Picture:", font=("Helvetica", 12))
        self.pic_path_lbl.grid(row=5, column=4, padx=10, pady=10, sticky="E")

        self.pic_path_entry = tk.Entry(frame, width=19, state="readonly")
        self.pic_path_entry.place(x=480, y=267)


        # Create Listboxes
        self.videos_listbox = Listbox(frame, width=40, height=12, selectmode="SINGLE", exportselection=0)
        self.videos_listbox.grid(row=1, column=0, columnspan=3, rowspan=5, padx=10, pady=10)
        self.videos_listbox.bind("<<ListboxSelect>>", self.__on_select)

        # Create video action buttons
        self.add_video_btn = tk.Button(frame, text="Add", width=6,command=self.__add_item)
        self.add_video_btn.grid(row=6, column=5, padx=10, pady=5)
        # self.add_video_btn.grid_remove()

        self.edit_video_btn = tk.Button(frame, text="Edit", width=6, command=self.__edit_item)
        self.edit_video_btn.grid(row=6, column=6, padx=10, pady=5)
        # self.edit_video_btn.grid_remove()

        self.delete_video_btn = tk.Button(frame, text="Delete", width=6, command=self.delete_video)
        self.delete_video_btn.grid(row=6, column=7, padx=10, pady=5)
        # self.delete_video_btn.grid_remove()

        # Create Back button at the bottom cente
        self.clear_all_btn = tk.Button(frame, text="Clear all", command=self.__clear_entries)
        self.clear_all_btn.grid(row=0, column=5, columnspan=3, pady=10)
        # self.clear_all_btn.grid_remove()
        tk.Button(frame, text="－",font=("Helvetica", 12), width=3, command=self.decrease_rate).place(x=623, y=162)
        tk.Button(frame, text="＋",font=("Helvetica", 12), width=3, command=self.increase_rate).place(x=673, y=162)
        self.load_path_btn = tk.Button(frame, text="Load", width=4, command=self.__ask_pic_path)
        self.load_path_btn.place(x=665, y=261)


        self.status_lbl = tk.Label(frame, text="P/s: Only possible to edit rating. \nIf you want to change the Name, or Director\nplease create new video with your changed and deleted the old-one <3", font=("Helvetica", 10), justify="left")
        self.status_lbl.place(x=15, y=295)
        self.load_videos()

    def __ask_pic_path(self):
        selected_video_index = self.videos_listbox.curselection()
        if not selected_video_index:
            messagebox.showerror("Warning", "Please choose a video to Load image.")
            return
        file_name = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png"),
                                                            ("All files", "*.*")])
        self.video_raw_path = file_name
        self.__load_pic_path(file_name)
    
    def __load_pic_path(self, file_name):
        if not file_name:
            self.pic_path_entry.config(state="normal")  
            self.pic_path_entry.delete(0, tk.END)      
            self.pic_path_entry.insert(0, "Not_Found")  
            self.pic_path_entry.config(state="readonly")     
            return
        
        file_name_without_extension, file_extension = os.path.splitext(os.path.basename(file_name)) #?
        self.pic_path_entry.config(state="normal")  
        self.pic_path_entry.delete(0, tk.END)      
        self.pic_path_entry.insert(0, file_name_without_extension)  
        self.pic_path_entry.config(state="readonly")

    def load_videos(self):
        self.videos_listbox.delete(0, tk.END)
        video_list = vid.list_all()
        set_text.set_content(self.videos_listbox, video_list)
        self.check_video_object.list_videos_clicked()
        self.create_list_object.load_videos()
        self.search_video_object.load_videos()
        self.video_raw_path = None
        
        # self.recently_deleted_object.show_video_in_bin()
    
    def __update_entry(self, entry, value):
        entry.delete(0, tk.END)
        entry.insert(0, value)

    def __on_select(self, event):
        selected_video_index = self.videos_listbox.curselection()
        if selected_video_index:
            self.selected_video = self.videos_listbox.get(selected_video_index[0]).strip()
            if self.selected_video == "":
                messagebox.showerror("error", "Error: Video ID out of range")
                return
            
            self.video_id = self.selected_video.split(" - ")[0]
            with open(vid.get_library_path(), 'r', newline='') as file:
                lines = csv.reader(file)
                for row in lines:
                    if row[0] == self.video_id:
                        video_name = row[1]
                        video_director = row[2]
                        video_rate = row[3]
                        video_count = row[4]
                        video_path = row[5]
                        self.save_video_path(video_path)
                        image_name_without_extension, image_extension = os.path.splitext(os.path.basename(video_path))
                        
                        self.__update_entry(self.name_entry, video_name)
                        self.__update_entry(self.director_entry, video_director)
                        self.__update_entry(self.rate_entry, video_rate)
                        self.__update_entry(self.count_entry, video_count)
                        self.pic_path_entry.config(state="normal")      
                        self.__update_entry(self.pic_path_entry, image_name_without_extension)
                        self.pic_path_entry.config(state="readonly")

    def save_video_path(self, video_path):
        self.video_raw_path = video_path
        return self.video_raw_path

    def __add_item(self):
        if not self.name_entry.get() and not self.director_entry.get() and not self.rate_entry.get() and not self.count_entry.get():
            messagebox.showerror("Warning", "Please input fully.")
            return
        video_name = self.name_entry.get()
        video_director = self.director_entry.get()
        video_rate = self.rate_entry.get()
        video_count = self.count_entry.get()
        video_path = self.pic_path_entry.get()
        
        if not self.video_raw_path:
            if video_path == "Not_Found":
                new_video_path = "Empty"
            elif video_path == "Empty":
                new_video_path = "Empty"
            elif not video_path:
                new_video_path = "Empty"
            else:
                video_path = self.save_video_path()
        else: new_video_path = self.video_raw_path
        next_video_id = vid.get_next_id()
        vid.add_new_video_in_library(next_video_id, video_name, video_director, video_rate, video_count, new_video_path)
        self.load_videos()
        self.search_video_object.load_videos()
        self.__clear_entries()

    def __edit_item(self):
        selected_video_index = self.videos_listbox.curselection()
        if not selected_video_index:
            messagebox.showerror("Warning", "Choose a video to edit.")
            return
        selected_video_index = selected_video_index[0]
        self.selected_video = self.videos_listbox.get(selected_video_index).strip()
        video_name = self.name_entry.get().strip()
        video_director = self.director_entry.get().strip()
        video_rate = self.rate_entry.get()
        video_count = self.count_entry.get()
        new_video_path = self.pic_path_entry.get()

        id = int(self.selected_video.split(" - ")[0])
        rate = len(self.selected_video.split(" - ")[3])
        with open(vid.get_library_path(), 'r', newline='') as file:
            lines = csv.reader(file)
            for row in lines:
                if row[0] == str(id):
                    old_video_path = str(row[5])
                    count = int(row[4])
                    if not self.video_raw_path:
                        if new_video_path == "Not_Found":
                            new_video_path = "Empty"
                        elif new_video_path == "Empty":
                            new_video_path = "Empty"
                        else: new_video_path = old_video_path
                    else: new_video_path = self.video_raw_path
        vid.edit_video_in_library(id, video_name, video_director, video_rate, rate, video_count, count, old_video_path,  new_video_path)
        self.load_videos()
        self.search_video_object.load_videos()

        self.videos_listbox.selection_set(selected_video_index) 
        self.videos_listbox.activate(selected_video_index)      # auto highlight underline selecion  
        self.videos_listbox.see(selected_video_index)           # auto move to selectiong
        # self.__clear_entries()


    def __clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.director_entry.delete(0, tk.END)
        self.rate_entry.delete(0, tk.END)
        self.count_entry.delete(0, tk.END)
        self.pic_path_entry.config(state="normal")  
        self.pic_path_entry.delete(0, tk.END)  
        self.pic_path_entry.config(state="readonly")  
        self.selected_video = None
        self.videos_listbox.selection_clear(0, tk.END)
        self.video_id = None


    def delete_video(self):
        selected_video_index = self.videos_listbox.curselection()
        if not selected_video_index:
            messagebox.showerror("Warning", "No video selected.")
            return
        
        video_id, video_name, video_director, video_rate = self.selected_video.split(" - ")
        video_rate = len(video_rate)
        with open(vid.get_library_path(), 'r', newline='') as file:
            lines = csv.reader(file)
            next(lines)
            for row in lines:
                if row[0] == str(video_id):
                    video_path = str(row[5])
        vid.delete_video_in_library(video_id, video_name, video_director, video_rate, video_path)

        # Remove video from all lists using delete_video method from create_video_list
        self.delete_video_in_all_list(video_id, video_name)
        messagebox.showinfo("Success", f"Video '{video_name}' have moved to Bin\n and deleted in all list successfully.")

        # Update all the Listbox
        self.load_videos()
        self.create_list_object.load_videos()
        self.create_list_object.update_list()
        self.search_video_object.load_videos()
        self.__clear_entries()


    def delete_video_in_all_list(self, video_id, video_name):
        for list_file in os.listdir(lis.get_list_library_path()):
            if not list_file.endswith(".csv"): continue
            list_file_name = list_file.rsplit(".", 1)[0]
            lis.delete_video(list_file_name, video_id)

    def reset_counting_all(self):
        with open(vid.get_library_path(), 'r', newline='') as file:
            lines = iter(file.readlines()) 

        updated_lines = []
        for row in lines:
            row = row.strip()  
            if not row: 
                continue
            
            fields = row.split(",")
            video_id = fields[0]  
            vid.set_rating(video_id, 0)
            fields[4] = '0'  
            updated_lines.append(",".join(fields))

        with open(vid.get_library_path(), 'w', newline='') as file: 
            file.writelines(line + "\n" for line in updated_lines)
        self.load_videos()
        self.search_video_object.load_videos()
        self.__clear_entries()
        messagebox.showinfo("success", "Reset all the couting time successfully")

    def decrease_rate(self):
        rate = self.rate_entry.get()
        if not rate:
            messagebox.showerror("Error", "Please select a video to increase the rating")
            return
        elif int(rate) == 1:
            messagebox.showerror("Error", "Minimum is 1 star")
            return
        rate = int(rate)
        rate -= 1 
        self.__update_entry(self.rate_entry, str(rate))
        self.__edit_item()
        # messagebox.showinfo("success", "-1 Star Successfully")


    def increase_rate(self):
        rate = self.rate_entry.get()
        if not rate:
            messagebox.showerror("Error", "Please select a video to increase the rating")
            return
        elif int(rate) == 5:
            messagebox.showerror("Error", "Maximum is 5 star")
            return
        rate = int(rate)
        rate += 1 
        self.__update_entry(self.rate_entry, str(rate))
        self.__edit_item()
        # messagebox.showinfo("success", "+1 Star Successfully")


