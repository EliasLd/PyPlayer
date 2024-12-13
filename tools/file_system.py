import os
import platform

# Contains essentials functionalities
# for fiding specific files/directories
# on Windows and Linux OS

def get_user_os() -> str:
    """
    Get the user operating system
    Returns:
        str: operating system name 
        (Windows, Linux, ...)
    """
    user_os = str(platform.system().lower())
    return user_os

def get_music_folder_name() -> str:
    """
    Get the basic/root music path depending 
    on the operating system.
    Returns:
        str: absolute path of music folder
    """
    user_os = get_user_os()
    username = os.getlogin()

    if "windows" in user_os or "win32" in user_os:
        # No language issue
        music_path = f'C:/Users/{username}/Music'

    else: 
        # Linux
        # Using the config file containing the path
        # of XDG directories
        dirs = os.path.expanduser(
                "~/.config/user-dirs.dirs"
        )
        try:
            # Reading the .dirs file
            with open(dirs, 'r') as f:
                for line in f:
                    if "XDG_MUSIC_DIR" in line:
                        # Get the absolute path
                        # of music folder
                        music_path = line.split('=')[1].strip('"')
                        break
        except FileNotFoundError:
            print("File user-dirs.dirs not found.")
            return None
        
    return music_path