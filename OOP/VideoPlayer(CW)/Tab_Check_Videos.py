# Import necessary libraries for GUI and image handling
import tkinter as tk                # tkinter provides tools for creating GUI elements
from Controling_Video_Library import vid        # Import video library functions from video_library.py
from PIL import Image, ImageTk       # PIL (Pillow) is used for image processing
from tkinter import Listbox, messagebox          # Import Listbox widget for displaying a list of items

# Function to set the content of a text area
def set_text(text_area, content):   
    text_area.delete("1.0", tk.END)  # Delete existing content from the first line to the end
    text_area.insert(1.0, content)   # Insert new content starting from the first line

class CheckVideos():
    def __init__(self, frame):
        self.frame = frame
        
        # Button to list all videos, triggers list_videos_clicked method when clicked
        list_videos_btn = tk.Button(frame, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10, sticky="W")

        # creat a clear button right to list all videos
        clear_btn = tk.Button(frame, text="Clear", command=self.clear_list)
        clear_btn.grid(row=0, column=1, padx=10, pady=10, sticky="W")

        # Label for video information
        tk.Label(frame, text="Video Information:").place(x=400, y=178)

        # Listbox to display a list of videos
        self.videos_listbox = Listbox(frame, width=40, height=12, selectmode="SINGLE", exportselection=0)
        self.videos_listbox.grid(row=1, column=0, columnspan=3, rowspan=3, padx=10, pady=10)
        self.videos_listbox.bind('<<ListboxSelect>>', self.__on_select)  # Bind selection event to method

        # Text widget to display selected video details
        self.video_txt = tk.Text(frame, width=30, height=5)
        self.video_txt.place(x=400, y=199)

        # Label to display the video image
        self.video_image = tk.Label(frame)
        self.video_image.place(x=400, y=20)

        # Populate the Listbox with videos on initialization
        self.list_videos_clicked()

    def clear_list(self):
        # Clear the Listbox and text widget
        self.video_txt.config(state="normal")
        set_text(self.video_txt, "")
        self.video_txt.config(state="disabled")
        self.video_image.config(image="")
        self.video_image.image = None

    def __on_select(self, event):
        # Get the index of the selected item and retrieve its string
        selected_index = self.videos_listbox.curselection()[0]
        video_str = self.videos_listbox.get(selected_index)
        key = video_str.split(" - ")[0]  # Extract the video ID from the selected item
        self.video_txt.config(state="normal")  # Enable text widget for editing
        try: 
            key = int(key)  # Convert key to integer
        except ValueError:
            messagebox.showerror('error', "sorry, you are selecting a blank...")
        name = vid.get_name(key)  # Get video name using the ID

        if name is None:
            # Set error message if video is not found
            set_text(self.video_txt, f"Video not found")
            return

        # Get additional details about the video
        director = vid.get_director(key)
        rating = vid.get_rating(key)
        play_count = vid.get_play_count(key)
        # Format the video details into a string
        video_details = f"Name: {name}.\nDirector: {director}.\nRating: {rating} star(s).\nPlays: {play_count} time(s)."
        # Update the text widget with video details
        set_text(self.video_txt, video_details)
        # Disable text widget after editing
        self.video_txt.config(state="disabled")

        # Update the video image based on the video ID
        self.update_video_image(key)

    def update_video_image(self, key):
        image_path = vid.get_image_path(key)  # Get the image path for the video

        try:
            # Open, resize, and display the image
            image = Image.open(image_path)       
            image = image.resize((270, 145))    # Resize the image to fit the label
            img = ImageTk.PhotoImage(image)     # Convert image to PhotoImage format
            self.update_image(img)              # Update the label with the image

        except FileNotFoundError:
            # Display error message if image is not available
            self.video_image.config(image='', text='Image not available :(')

    def update_image(self, img):
        self.video_image.config(image=img)  # Set the image in the label
        self.video_image.image_ref = img        # Store a reference to the image to prevent garbage collection

    def list_videos_clicked(self):
        video_list = vid.list_all()  # Retrieve a list of all videos
        lines = video_list.split('\n')  # Split the list into lines
        self.videos_listbox.delete(0, tk.END)  # Clear existing items in the Listbox
        # Add each video to the Listbox
        for line in lines:
            self.videos_listbox.insert(tk.END, f"{line}\n")
