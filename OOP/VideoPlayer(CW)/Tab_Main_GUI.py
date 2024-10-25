import tkinter as tk
import Tab_Check_Videos as CheckVideos
import Tab_Create_Video_List as CreateList
import Tab_Update_Videos as UpdateVideos
import Tab_Search_Video as SearchVideos
import Tab_Recently_Deleted as RecentlyDeleted
import Source_Font_Manager as fonts

from tkinter import ttk


def set_content(listbox, content):
    listbox.delete(0, tk.END)
    
    for line in content.split('\n'):
        if line.strip():
            listbox.insert(tk.END, line)

class VideoGUIApp():
    def __init__(self, mainWindow):
        self.mainWindow = mainWindow
        self.mainWindow.title("My Video GUI App")
        
        self.tab_control = ttk.Notebook()

        # Create tabs for different functionalities
        self.check_videos_tab = ttk.Frame(self.tab_control)  
        self.create_lists_tab = ttk.Frame(self.tab_control)
        self.update_videos_tab = ttk.Frame(self.tab_control)
        self.search_videos_tab = ttk.Frame(self.tab_control)
        self.recently_deleted_tab = ttk.Frame(self.tab_control)
        
        self.tab_control.add(self.check_videos_tab, text="Check Videos")
        self.tab_control.add(self.create_lists_tab, text="Create Lists") 
        self.tab_control.add(self.update_videos_tab, text="Update Videos")
        self.tab_control.add(self.search_videos_tab, text="Search Videos")
        self.tab_control.add(self.recently_deleted_tab, text="Recently Deleted")
        self.tab_control.pack(fill="both") 

        # Initialize interfaces in the respective tabs
        self.check_videos_object = CheckVideos.CheckVideos(self.check_videos_tab)
        self.create_list_object = CreateList.CreateVideoList(self.create_lists_tab, self.check_videos_object)
        self.search_videos_object = SearchVideos.SearchVideos(self.search_videos_tab)
        self.update_videos_object = UpdateVideos.UpdateVideos(self.update_videos_tab, self.check_videos_object, self.create_list_object, self.search_videos_object)
        self.recently_deleted_object = RecentlyDeleted.RecentlyDeleted(self.recently_deleted_tab, self.update_videos_object)


    def run(self):
        self.mainWindow.mainloop()

if __name__ == "__main__":
    main = tk.Tk()
    fonts.configure()  # Configure fonts before initializing the app
    app = VideoGUIApp(main)
    main.geometry("750x400")
    style = ttk.Style()
    style.configure("TNotebook.Tab", padding=[10, 5])  # Adjust tab padding
    app.run()
