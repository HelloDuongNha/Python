import tkinter as tk
import csv
import os
import Tab_Main_GUI as set_text

from tkinter import Listbox, simpledialog, messagebox
from Controling_Video_Library import vid
from Controling_List_Library import lis



class CreateVideoList:
    def __init__(self, frame, check_videos_object):
        self.frame = frame
        self.check_videos_object = check_videos_object
        self.current_selected_list = None
        self.in_file = False

        # def create_button(self):
            # Create buttons above the left Listbox
        self.view_video_btn = tk.Button(frame, text="List All Videos", command=self.load_videos)
        self.view_video_btn.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        self.create_list_btn = tk.Button(frame, text="Create List", width=10, command= self.create_new_list)
        self.create_list_btn.grid(row=0, column=4, padx=10, pady=10, sticky="W")

        self.play_list_btn = tk.Button(frame, text="Play List", width=10, command=self.play_list)
        self.play_list_btn.grid(row=1, column=5, padx=10, pady=10, sticky="W")
        self.play_list_btn.grid_remove()

        self.rename_list_btn = tk.Button(frame, text="Rename list", width=10, command=self.rename_list)
        self.rename_list_btn.grid(row=2, column=5, padx=10, pady=10, sticky="W")
        self.rename_list_btn.grid_remove()

        self.delete_list_btn = tk.Button(frame, text="Delete list", width=10, command=self.delete_list)
        self.delete_list_btn.grid(row=3, column=5, padx=10, pady=10, sticky="W")
        self.delete_list_btn.grid_remove()

        # Create Listboxes
        self.videos_listbox = Listbox(frame, width=40, height=12, selectmode="SINGLE", exportselection=0)
        self.videos_listbox.grid(row=1, column=0, columnspan=3, rowspan=3, padx=10, pady=10)
        self.videos_listbox.bind('<<ListboxSelect>>', self.on_videos_select)

        self.lists_listbox = tk.Listbox(frame, width=21, height=12, selectmode="SINGLE", exportselection=0)
        self.lists_listbox.grid(row=1, column=3, columnspan=2, rowspan=3, padx=10, pady=10)
        self.lists_listbox.bind('<<ListboxSelect>>', self.on_folder_select)
        self.lists_listbox.bind('<Double-1>', self.open_list)
        

        # Create video action buttons
        self.add_video_btn = tk.Button(frame, text="add video", width=10, command=self.add_video)
        self.add_video_btn.grid(row=0, column=1, padx=10, pady=10, sticky="W")
        self.add_video_btn.grid_remove()

        self.delete_video_btn = tk.Button(frame, text="delete video", width=10, command=self.delete_btn)
        self.delete_video_btn.grid(row=1, column=5, padx=10, pady=10, sticky="W")
        self.delete_video_btn.grid_remove()

        self.status_lbl = tk.Label(frame, text="Tips: Doule-click on a list to go inside a list first,\nthen you can add/delete your video :3", font=("Helvetica", 10), justify="left")
        self.status_lbl.place(x=15, y=295)

        self.list_info_lbl = tk.Label(frame, text="", font=("Helvetica", 12))
        self.list_info_lbl.grid(row=0, column=3, padx=10, pady=10, sticky="SW")

        # Create Back button at the bottom cente
        self.back_btn = tk.Button(frame, text="back", command=self.back_to_list)
        self.back_btn.grid(row=4, column=3, columnspan=2, padx=10, sticky="N")
        self.back_btn.grid_remove()

        self.load_videos()   # load all video in library
        self.update_list()                      # load all list






####### show info in listbox
    def load_videos(self): # use to show/ refresh all the videos in the Listbox/ text area
        video_list = vid.list_all()
        set_text.set_content(self.videos_listbox, video_list)
        self.check_videos_object.list_videos_clicked()

    def update_list(self):
        self.lists_listbox.delete(0, tk.END)
        lis.display_all_list(self.lists_listbox)



####### create new list
    def create_new_list(self):
        try:
            file_name = simpledialog.askstring("Input", "Enter list name:")
            if not file_name.strip():
                messagebox.showerror("Error", "Please enter a file name.")
                return
            
            file_name = file_name.strip() 
            file_name += ".csv"
            list_library_path = lis.get_list_library_path()
            new_file_path = os.path.join(list_library_path, file_name)
            
            if os.path.exists(new_file_path):
                messagebox.showerror("Warning", f"File '{file_name}' already exists.")
                return
            
            with open(new_file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
            messagebox.showinfo("Success", f"File '{file_name}' created successfully.")
            self.update_list()
        except PermissionError as e:
            messagebox.showerror("Error", f"Permission denied: {e}")

####### selecting 1 time
    def on_folder_select(self, event):
        if not self.in_file:
            self.rename_list_btn.grid()
            self.delete_list_btn.grid()
            self.play_list_btn.grid()
            self.add_video_btn.grid_remove()
            selection = self.lists_listbox.curselection()
            if selection:
                sub_variable = self.lists_listbox.get(selection[0]).strip()
                listbox_id, listbox_name = sub_variable.split(" - ")
                self.current_selected_list = listbox_name
        else:
            self.delete_video_btn.grid()
            self.add_video_btn.grid_remove()

    def on_videos_select(self, event):
        if self.in_file:
            self.add_video_btn.grid()
            self.delete_video_btn.grid_remove()
            self.rename_list_btn.grid_remove()
            self.delete_list_btn.grid_remove()
            self.play_list_btn.grid_remove()
        else:
            messagebox.showwarning("warning", "Please choose a List first")


###### enter the list
    def open_list(self, event):
        if self.in_file:
            return
        else:   selected_list = self.lists_listbox.curselection()
        if selected_list:
            sub_variable = self.lists_listbox.get(selected_list[0]).strip()
            listbox_name = sub_variable.split(" - ")[1]
            self.current_selected_list = listbox_name
            self.show_folder_contents(self.current_selected_list)
            

    def show_folder_contents(self, folder_name):
        self.rename_list_btn.grid_remove()
        self.delete_list_btn.grid_remove()
        self.play_list_btn.grid_remove()
        self.add_video_btn.grid_remove()
        self.delete_video_btn.grid_remove()
        self.create_list_btn.grid_remove()
        self.back_btn.grid()

        self.lists_listbox.delete(0, tk.END)
        lis.show_video_in_list(self.lists_listbox, folder_name)
        self.list_info_lbl.configure(text=f"List name: {folder_name} ")
        self.in_file = True


##### go back
    def back_to_list(self):
        self.update_list()
        self.create_list_btn.grid()
        self.back_btn.grid_remove()
        self.add_video_btn.grid_remove()
        self.delete_video_btn.grid_remove()
        self.list_info_lbl.configure(text=f"")
        self.current_selected_list = None
        self.in_file = False




######## add video
    def add_video(self):
        selected_video_index = self.videos_listbox.curselection()
        selected_video = self.videos_listbox.get(selected_video_index).strip()
        list_file_path = lis.list_direction(self.current_selected_list)

        if selected_video == "":
            messagebox.showerror("Warning", "Selected index is out of range.")
            return
        if not os.path.exists(list_file_path):
            messagebox.showerror("Error", "The list file does not exist.")
            return
        
        video_id, video_name, director, rating = selected_video.split(' - ')
        with open(list_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            if lis.video_exist_in_list(self.current_selected_list, video_name, director):
                messagebox.showerror("Fail", f"Video '{video_name}' by '{director}' has already exist in this list.")
                return
            
            writer.writerow([video_id, video_name, director, len(rating)])
            messagebox.showinfo("Success", f"Video '{video_name}' added to the list '{self.current_selected_list}' successfully.")

        self.show_folder_contents(self.current_selected_list)

    def get_index_selected(self, which_listbox):
        selected_index = which_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Warning", "No video selected.")
            return
        selected_index = selected_index[0]
        return selected_index

    def delete_btn(self):
        video_id = self.get_index_selected(self.lists_listbox)
        real_video_id = lis.convert_lixboxIndex_to_RealIndex(self.current_selected_list, video_id)
        lis.delete_video(self.current_selected_list, real_video_id)
        self.show_folder_contents(self.current_selected_list)
        video_name = lis.get_name()
        messagebox.showinfo("Success", f"Video '{video_name}' deleted from the list successfully.")

    def set_current_selected_list(self):
        return self.current_selected_list

##### play list
    def play_list(self):
        if not self.current_selected_list:
            messagebox.showerror("Warning", "Please double-click to go inside the list first.")
            return
        
        list_file_path = lis.list_direction(self.current_selected_list)
        if not os.path.exists(list_file_path):
            messagebox.showerror("Error", "The list file does not exist.")
            return
        with open(list_file_path, 'r', newline='') as file:
            lines = csv.reader(file)    # read all line = all videos that have in that play list
            for row in lines:
                if row == []: 
                    continue
                try:
                    video_id = int(row[0])
                except ValueError:
                    messagebox.showerror("Error", f"Invalid video ID in row: {row}")
                    return
                vid.increment_play_count(video_id)  # increase that id in the library
        
            messagebox.showinfo("Success", f"Playlist | {self.current_selected_list} | has been played and play count incremented.")
            vid.save_library()
            self.check_videos_object.list_videos_clicked()

    def delete_list(self):
        if not self.current_selected_list:
            messagebox.showerror("Warning", "Please select a list to delete.")
            return
        
        list_file_path = lis.list_direction(self.current_selected_list)
        if not os.path.exists(list_file_path):
            messagebox.showerror("Error", "The list file does not exist.")
            return
        
        os.remove(list_file_path)
        messagebox.showinfo("Success", f"List '{self.current_selected_list}' has been deleted.")
        self.update_list()
        self.current_selected_list = None

    def rename_list(self):
        if not self.current_selected_list:
            messagebox.showerror("Warning", "Please select a list to rename.")
            return

        new_name = simpledialog.askstring("Input", "Enter new list name:")
        if not new_name:
            messagebox.showerror("Warning", "Please enter a new name.")
            return
        
        new_name = new_name.strip() + ".csv"
        list_library_path = lis.get_list_library_path()
        new_file_path = os.path.join(list_library_path, new_name)
        
        if os.path.exists(new_file_path):
            messagebox.showerror("Warning", "A list with this name already exists.")
            return
        
        old_file_path = lis.list_direction(self.current_selected_list)
        os.rename(old_file_path, new_file_path)
        
        messagebox.showinfo("Success", f"List '{self.current_selected_list}' has been renamed to '{new_name}'.")
        self.update_list()
        self.current_selected_list = new_name

