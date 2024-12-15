from tkinter import PhotoImage
import customtkinter

# This file contains settings
# for the application

# System settings
# Identical as user's theme
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Customize app frame
        self.title("PyPlayer")
        icon = PhotoImage(file="assets/music-notes.png")
        self.after(201, lambda :self.iconphoto(False, icon))
        self.geometry("720x480")

# Create and run the app
app = App()
app.mainloop()