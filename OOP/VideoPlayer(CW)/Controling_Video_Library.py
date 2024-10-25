from Resource_Library_Item import LibraryItem
import csv
import os
from tkinter import messagebox

class VideoLibrary:
    def __init__(self):
        self.csv_file = "C:\WorkSpace\OOP\VideoPlayer\data\Videos.csv"         # please change the path to the correct path after dowloading if you want to run <3
        self.bin_file = "C:\WorkSpace\OOP\VideoPlayer\data\Recycle_bin.csv"     # please change the path to the correct path after dowloading if you want to run <3
        self.list_all()

    def get_bin_path(self):
        return self.bin_file

    def list_all(self):
        try:
            self.library = {}
            self.sort_csv_by_id()
            with open(self.csv_file, "r", newline='') as f:
                lines = csv.reader(f)
                for row in lines:
                    if not row: 
                        continue
                    video_id = int(row[0])
                    name = row[1]
                    director = row[2]
                    rating = int(row[3])
                    count = int(row[4])
                    path = str(row[5])
                    video = LibraryItem(video_id, name, director, rating, count, path)
                    self.library[video_id] = video
            output = ""
            for key in self.library:
                item = self.library[key]
                output += f" {key} - {item.info()}\n"
            return output
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    
    def sort_csv_by_id(self):
        # Read the CSV file
        with open(self.csv_file, mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)  # Read the rest of the data
            rows.sort(key=lambda x: int(x[0])) # Sort the rows by the ID column (index 0)

        # Write the sorted data back to a new CSV file
        with open(self.csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(rows)  # Write the sorted rows

    def get_library_path(self):
        return self.csv_file   # output = path

    def get_id(self, key):
        try:
            item = self.library[key]
            return item.id
        except KeyError:
            return None

    def get_name(self,key):
        try:
            item = self.library[key]
            return item.name
        except KeyError:
            return None


    def get_director(self, key):
        try:
            item = self.library[key]
            return item.director
        except KeyError:
            return None


    def get_rating(self, key):
        try:
            item = self.library[key]
            return item.rating
        except KeyError:
            return -1


    def set_rating(self, key, rating):
        try:
            item = self.library[key]
            item.rating = rating
        except KeyError:
            return


    def get_play_count(self, key):
        try:
            item = self.library[key]
            return item.play_count
        except KeyError:
            return -1


    def increment_play_count(self, key):
        try:
            item = self.library[key]
            item.play_count += 1
        except KeyError:
            return


    def save_library(self):
        with open(self.csv_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            for key in self.library:
                video = self.library[key]
                writer.writerow([video.id, video.name, video.director, video.rating, video.play_count, video.image_path])


    def get_next_id(self):
        highest_id = 0
        with open(self.csv_file, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    current_id = int(row[0])
                    if current_id > highest_id:
                        highest_id = current_id
        return highest_id + 1

    def remove_video(self, ID):
        for item in self.library:
            video = self.library[item]
            if video.id == int(ID):
                del self.library[int(ID)]
                return

    def update_after_delete(self, ID):
        self.list_all()
        self.remove_video(ID)
        self.save_library()

    def update_after_add(self, ID, Name, Director, Rating, Count, path):
        self.list_all()
        new_video = LibraryItem(ID, Name, Director, Rating, Count, path)
        self.remove_video(ID)
        self.library[ID] = new_video
        self.save_library()

    def check_id_existion(self, place_to_check, id_to_check):
        if os.path.isdir(place_to_check):
            messagebox.showerror('Error', f'{place_to_check} is not a file!')
            return
        with open(place_to_check, "r", newline='') as f:
            lines = csv.reader(f)
            for row in lines:
                if len(row) >=1 and row[0] == id_to_check:
                    return True    
        return False

    def check_existion(self, place_to_check, name_to_check, director_to_check):
        if os.path.isdir(place_to_check):
            messagebox.showerror('Error', f'{place_to_check} is not a file!')
            return
        with open(place_to_check, "r", newline='') as f:
            lines = csv.reader(f)
            for row in lines:
                if str(row[1]) == str(name_to_check) and str(row[2]) == str(director_to_check):
                    return True
        return False


    def add_new_video_in_library(self, next_video_id, video_name, video_director, video_rate, video_count, video_path):
        try:
            if self.check_existion(self.csv_file, video_name, video_director):
                raise ValueError(f"Video '{video_name}' by '{video_director}' has already exist in this list.")
            
            LibraryItem(next_video_id, video_name, video_director, video_rate, video_count, video_path)
            with open(self.csv_file, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([next_video_id, video_name, video_director, video_rate, video_count,video_path])

            messagebox.showinfo("Success", f"Video '{video_name}' added to the list successfully.")
            self.update_after_add(next_video_id, video_name, video_director, video_rate, video_count, video_path)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def edit_video_in_library(self, id, video_name, video_director, new_rate, old_rate, video_count, count, old_video_path, new_video_path):
        try: 
            if self.check_existion(self.csv_file,video_name,video_director) and str(new_rate) == str(old_rate) and str(old_video_path) == str(new_video_path) and str(video_count) == str(count):
                raise ValueError(f"You have't changed anything...")            
            elif str(video_count) != str(count):
                raise ValueError(f"sorry, Editing the Counting is not posible")
            elif not self.check_existion(self.csv_file, video_name, video_director):
                raise ValueError(f"sorry, Editing the Name and Director is not posible.\n Please add another Video and delete this video to change.")
            elif self.check_existion(self.csv_file, video_name, video_director) and new_rate == old_rate and old_video_path == new_video_path:
                raise ValueError(f"Video '{video_name}' by '{video_director}' has already exist in this list.")
            with open(vid.get_library_path(), 'r', newline='') as file:
                lines = file.readlines()
            modified_lines = []
            for line in lines:
                line_list = line.strip().split(',')         # split to check
                if line_list[0] == str(id):       
                    line_list[1] == str(video_name).strip()
                    line_list[2] == str(video_director).strip()
                    line_list[3] = str(new_rate)
                    line_list[4] = str(video_count)
                    line_list[5] = str(new_video_path)
                new_line = ','.join(map(str, line_list)) + '\n' # recovery
                modified_lines.append(new_line)                 # add again
            LibraryItem(id, video_name, video_director, new_rate, video_count, new_video_path)
            with open(vid.get_library_path(), 'w', newline='') as file:
                file.writelines(modified_lines)                 # paste
            messagebox.showinfo("Success", f"Video '{video_name.strip()}' edited successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def delete_video_in_library(self, video_id, video_name, video_director, video_rate, video_path):
        # Add the video to the recently_deleted list
        if not self.check_existion(self.bin_file, str(video_name), str(video_director)):  # if it have the same in bin, it wont add 
            with open(self.bin_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([video_id, video_name, video_director, video_rate, 0, video_path])
        # Remove video from the main library
        with open(self.csv_file, 'r', newline='') as file:
            lines = file.readlines()
        updated_lines = []
        for line in lines:
            if not line.startswith(str(video_id)):
                updated_lines.append(line)
        with open(vid.get_library_path(), 'w', newline='') as file:
            file.writelines(updated_lines)
        self.update_after_delete(video_id)
        # messagebox.showinfo("Success", f"Video '{video_name}' have moved to Bin successfully.")

    def get_image_path(self, key):
        try:
            item = self.library[key]
            return item.image_path.strip()
        except KeyError:
            return None



vid = VideoLibrary()
