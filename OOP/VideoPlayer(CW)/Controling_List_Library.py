import tkinter as tk
import csv
import os
import Tab_Main_GUI as set_text

from Controling_Video_Library import vid
from tkinter import messagebox
from Resource_Library_Item import LibraryItem


class List:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f" {self.name} "

class ListLibrary:
    def __init__(self):
        self.parent_folder = "C:\WorkSpace\OOP\VideoPlayer\lists_folder"        # please change the path to the correct path after dowloading if you want to run <3
        # self.existion = False

    def list_all(self):
        output = ""
        auto_number = 1
        for key in self.library:
            item = self.library[key]
            output += f" {auto_number} - {item.name_info()}\n"
            auto_number += 1
        return output
    
    def display_all_list(self, area):
        output = ""
        auto_number = 1
        for file in os.listdir(self.parent_folder):
            if file.endswith('.csv'):
                file_name_without_extension = os.path.splitext(file)[0].strip()
                output = f" {auto_number} - {file_name_without_extension}"
                area.insert(tk.END, output)
                auto_number += 1

    def get_list_library_path(self):
        return self.parent_folder


    def list_direction(self, list_name):
        selected_file = list_name.strip() + ".csv"
        current_opened_file = os.path.join(self.parent_folder, selected_file)
        return current_opened_file    # output = path
    
    def show_video_in_list(self, area, list_name):
        self.library = {}
        file_path = self.list_direction(list_name)
        if not os.path.exists(file_path):
            set_text.set_content(area, "File not found")
            return
        
        with open(file_path, "r", newline='') as f:
            lines = csv.reader(f)
            for row in lines:
                # if  not row:
                #     set_text.set_content(area, "List is empty")
                #     return
                if len(row) >= 4:
                    video = LibraryItem(row[0], row[1], row[2], row[3], 0)
                    self.library[int(row[0])] = video
        content = self.list_all()
        set_text.set_content(area, content)

    def video_exist_in_list(self, name_list_to_get_path, name_to_check, director_to_check):
        file_path = self.list_direction(name_list_to_get_path)
        if not os.path.exists(file_path):
            return False
        
        return vid.check_existion(file_path, name_to_check, director_to_check)

    def convert_lixboxIndex_to_RealIndex(self, list_name, listbox_index):
        list_file_path = lis.list_direction(list_name)
        with open(list_file_path, 'r', newline='') as file:
            lines = file.readlines() 
            for row in lines:
                if not row: 
                    continue
        string = lines[listbox_index]
        video_id, self.video_name, director, rate = string.split(",")
        return video_id

    def delete_video(self, list_to_delete, video_id):
        list_file_path = lis.list_direction(list_to_delete)
        if list_file_path.endswith(".csv.csv"):
            list_file_path = list_file_path[:-4]
        if not os.path.exists(list_file_path):
            messagebox.showerror("Error", "The list file does not exist.")
            return
        
        with open(list_file_path, 'r', newline='') as file:
            lines = file.readlines()
            for row in lines:
                if not row: 
                    continue
        updated_lines = []
        for line in lines:
            if not line.startswith(str(video_id)):
                updated_lines.append(line)
        with open(list_file_path, 'w', newline='') as file:
            file.writelines(updated_lines)

    def get_name(self):
        return self.video_name


lis = ListLibrary()
