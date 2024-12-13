from tkinter import PhotoImage
import customtkinter

# This file contains basic settings
# for the application

# System settings
# Identical as user's theme
customtkinter.set_appearance_mode("System")

# Create the app frame
app = customtkinter.CTk()
app.geometry("720x480")

# Customize app frame
app.title("PyPlayer")
icon = PhotoImage(file="assets/music-notes.png")
app.after(201, lambda :app.iconphoto(False, icon))

# Run the app
app.mainloop()