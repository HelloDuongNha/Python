import tkinter as tk
import csv
import Tab_Main_GUI as set_text
import os
from tkinter import messagebox
from Controling_Video_Library import vid
from Resource_Library_Item import LibraryItem
from PIL import Image, ImageTk



class RecentlyDeleted:
    def __init__(self, frame, update_videos_object):
        self.frame = frame
        self.update_videos_object = update_videos_object

        # self.view_video_btn = tk.Label(frame, text="Recently Deleted Video ", font=("Helvetica", 12))
        # self.view_video_btn.grid(row=0, column=0, padx=10, pady=10, sticky="S")

        self.view_video_btn = tk.Button(frame, text="Refresh the List", width=15, command=self.show_video_in_bin)
        self.view_video_btn.grid(row=0, column=0, padx=10, pady=10, sticky="N")

        self.videos_listbox = tk.Listbox(frame, width=50, height=12, selectmode="SINGLE", exportselection=0)
        self.videos_listbox.grid(row=1, column=0, columnspan=3, rowspan=4, padx=10, pady=10, sticky="S")
        self.videos_listbox.bind('<<ListboxSelect>>', self.__on_select)
        
        self.delete_all_button = tk.Button(frame, text="Delete All", width=12, command=self.delete_all)
        self.delete_all_button.grid(row=0, column=2, padx=10, pady=10, sticky="N")

        self.recovery_all_button = tk.Button(frame, text="Recover All", width=12, command=self.recover_all)
        self.recovery_all_button.grid(row=0, column=1, padx=10, pady=10, sticky="N")

        self.delete_video_button = tk.Button(frame, text="Delete Video", width=12, command=self.delete_button)
        self.delete_video_button.place(x=610, y=262)
        self.delete_video_button.place_forget()

        self.recovery_video_button = tk.Button(frame, text="Recover Video", width=12, command=self.recover_button)
        self.recovery_video_button.place(x=480, y=262)
        self.recovery_video_button.place_forget()
        tk.Label(frame, text="Please press the Refresh Button to see the list after deleting any video\n thanks <3.", font=("Helvetica", 12), justify="center").place(x=15, y=303)

        self.video_image = tk.Label(frame)
        self.video_image.place(x=480, y=61)
        self.video_image.place_forget()
        self.show_video_in_bin()


    def list_all(self): # list và videos đều có list all, nên cho thừa kế.
        output = ""
        for key in self.library:
            item = self.library[key]
            output += f" {key} - {item.info()}\n"
        return output

    def show_video_in_bin(self):
        self.library = {}
        bin_path = vid.get_bin_path()
        
        if not os.path.exists(bin_path):
            set_text.set_content(self.videos_listbox, "File not found")
            return
        
        with open(bin_path, "r", newline='') as f:
            lines = csv.reader(f)
            for row in lines:
                if not row:  
                    continue
                if len(row) >= 5:  
                    video_id = int(row[0])
                    video_name = row[1]
                    video_director = row[2]
                    video_rate = int(row[3])
                    video_count = int(row[4])
                    video = LibraryItem(video_id, video_name, video_director, video_rate, video_count)
                    self.library[video_id] = video
        self.delete_video_button.place_forget()
        self.recovery_video_button.place_forget()
        self.video_image.place_forget()

        content = self.list_all()
        set_text.set_content(self.videos_listbox, content)
        self.update_videos_object.load_videos()


    def __on_select(self, event):
        selected_video_index = self.videos_listbox.curselection()
        if selected_video_index:
            self.delete_video_button.place(x=610, y=262)
            self.recovery_video_button.place(x=480, y=262)
            self.video_image.place(x=480, y=61)
            self.selected_video = self.videos_listbox.get(selected_video_index[0]).strip()
            if self.selected_video == "":
                messagebox.showerror("error", "Error: Video ID out of range")
                # self.__clear_entries()
                return
            self.old_video_id, self.video_name, self.video_director, self.video_rate = self.selected_video.split(" - ")
            with open(vid.get_bin_path(), 'r', newline='') as file:
                lines = csv.reader(file)
                for row in lines:
                    if str(row[0]) == str(self.old_video_id):
                        self.video_path = str(row[5])
            self.update_video_image()

    def update_video_image(self):
        try:
            image = Image.open(self.video_path)               # ex to config/update 
            image = image.resize((246, 178))
            img = ImageTk.PhotoImage(image)
            self.update_image(img)

        except Exception as e:
            # Set an error message in the label if the image is not available
            self.video_image.config(image='', text='Image not available :(...')

    def update_image(self, img):
        self.video_image.config(image=img)
        self.video_image.image = img

    def check_id_on_selected(self, old_video_id):
        # Add the video to the recently_deleted list
        if vid.check_id_existion(vid.get_library_path(), old_video_id):  # if it have the same in library id, it will turn to next id automaticaly
            return vid.get_next_id()
        return old_video_id


    def recover_button(self):
        # selected_video_index = self.videos_listbox.curselection()
        # if not selected_video_index:
        #     messagebox.showinfo("Error", "Please select a video to delete")
        #     return
        self.recover_video(self.old_video_id, self.video_name, self.video_director, self.video_rate, self.video_path)
        messagebox.showinfo("Success", f"video: {self.video_name} have been recovered successfully.")
        self.show_video_in_bin()

    def recover_video(self, old_video_id, video_name, video_director, video_rate, video_path):
        new_video_id = self.check_id_on_selected(old_video_id)
        with open(vid.get_library_path(), "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([new_video_id, video_name, video_director, len(video_rate), 0, video_path])
        # Remove video from the main library
        self.delete_video(old_video_id)

    def recover_all(self):
        with open(vid.get_bin_path(), 'r', newline='') as file:
            lines = file.readlines()
            for row in lines:
                if not row:  # Bỏ qua các dòng trống
                    continue
                if len(row) >= 5:  # Đảm bảo rằng tất cả các cột
                    video_id, video_name, video_director, video_rate, video_count, video_path = row.split(",")
                    video_path = video_path.strip()
                    self.recover_video(video_id, video_name, video_director, video_rate, video_path)
                    self.delete_video(video_id)
        messagebox.showinfo("Success", "All videos have been recovered successfully.")
        self.show_video_in_bin()

    def delete_button(self):
        # selected_video_index = self.videos_listbox.curselection()
        # if not selected_video_index:
        #     messagebox.showinfo("Error", "Please select a video to delete")
        #     return
        self.delete_video(self.old_video_id)
        messagebox.showinfo("Success", f"Video '{self.video_name}' have deleted forever successfully.")
        self.show_video_in_bin()

    def delete_video(self, old_video_id):
        # Remove video from the main library
        with open(vid.get_bin_path(), 'r', newline='') as file:
            lines = file.readlines()
        updated_lines = []
        for line in lines:
            if not line.startswith(str(old_video_id)):
                updated_lines.append(line)
        with open(vid.get_bin_path(), 'w', newline='') as file:
            file.writelines(updated_lines)

    def delete_all(self):
        with open(vid.get_bin_path(), 'r', newline='') as file:
            lines = file.readlines()
            for row in lines:
                if not row:  # Bỏ qua các dòng trống
                    continue
                if len(row) >= 5:  # Đảm bảo rằng tất cả các cột
                    video_id = row.split(",")[0]
                    self.delete_video(video_id)
        messagebox.showinfo("Success", "All videos deleted forever successfully.")
        self.show_video_in_bin()


