import customtkinter

from components.file_menu import FileMenu

class NavBar(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)   

        self.pack(side="top", fill="x")

        self.file_menu = None
        self.add_buttons()
    
    def add_buttons(self) -> None:
        """
        Creates and add buttons to navbar
        """
        # File button
        file_button = customtkinter.CTkButton(
            self, 
            text="File",
            width=20,
            height=15,
            fg_color="transparent",
            hover_color="grey",
            corner_radius=0,
            command=self.toggle_file_menu
        )

        # Settings button
        settings_button = customtkinter.CTkButton(
            self,
            text="Settings",
            width=20,
            height=15,
            fg_color="transparent",
            hover_color="grey",
            corner_radius=0
        )
        # Help button
        help_button = customtkinter.CTkButton(
            self,
            text="Help", 
            width=20, 
            height=15, 
            fg_color="transparent",
            hover_color="grey",
            corner_radius=0
        )

        # horizontally pack buttons
        file_button.pack(side="left", pady=1, padx=5)
        settings_button.pack(side="left", pady=1, padx=5)
        help_button.pack(side="left", pady=1, padx=5)
    
    def toggle_file_menu(self) -> None:
        """
        toggle the display of the
        file context menu
        """
        if self.file_menu is None:
            # Create and display the menu
            self.file_menu = FileMenu(self.master)
            self.file_menu.place(x=25, y=50)
        else:
            # Remove the menu if already displayed
            self.file_menu.destroy()
            self.file_menu = None

