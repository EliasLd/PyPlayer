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
        (Windows, Linux, darwin, ...)
    """
    user_os = str(platform.system().lower())
    return user_os

def get_music_folder_name() -> str:
    """
    [ LINUX ONLY ]
    Get the exact name of the music name 
    to avoid error caused by language. 
    Returns:
        str: name of the music folder
    """
    # Using the config file containing the path
    # of XDG directories
    dirs = os.path.expanduser(
            "~/.config/user-dirs.dirs")
    music_path = None

    try:
        # Reading the .dirs file
        with open(dirs, 'r') as f:
            for line in f:
                if "XDG_MUSIC_DIR" in line:
                    # Get the name of the 
                    # music folder
                    music_path = os.path.basename(
                        line.split('=')[1].strip('"')
                    )
                    break
    except FileNotFoundError:
        print("File user-dirs.dirs not found.")
        return None
    
    return music_path


def get_root_music_path(user_os: str) -> str:
    """
    Get the basic/root music path depending on the
    operating system.
    Returns:
        str: absolute path of music folder location
    """
    # First get the username
    username = os.getlogin()
    if "windows" in user_os or "win32" in user_os:
        music_path = 'C:/Users/{}/Music'.format(username)
    else: # Linux, darwin, java...
        music_path = '/home/'