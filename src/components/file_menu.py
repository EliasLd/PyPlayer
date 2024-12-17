import customtkinter

class FileMenu(customtkinter.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.configure(fg_color="grey", corner_radius=0)

        self.add_menu_items()

    def add_menu_items(self):
        """
        Creates and add options to file context menu
        """
         # Option 1
        new_button = customtkinter.CTkButton(
            self, 
            text="New File",
            width=120,
            height=30,
            fg_color="transparent",
            hover_color="lightgrey",
            corner_radius=5
        )
        new_button.pack(pady=2, padx=5, fill="x")

        # Option 2
        open_button = customtkinter.CTkButton(
            self, 
            text="Open File",
            width=120,
            height=30,
            fg_color="transparent",
            hover_color="lightgrey",
            corner_radius=5
        )
        open_button.pack(pady=2, padx=5, fill="x")

        # Option 3
        exit_button = customtkinter.CTkButton(
            self, 
            text="Exit",
            width=120,
            height=30,
            fg_color="transparent",
            hover_color="lightgrey",
            corner_radius=5
        )
        exit_button.pack(pady=2, padx=5, fill="x")