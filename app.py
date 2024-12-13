import tkinter
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

# Run the app
app.mainloop()