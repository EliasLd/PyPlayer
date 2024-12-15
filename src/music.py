from mutagen.mp3 import MP3
from mutagen.id3 import ID3, TIT2, TPE1, TALB, APIC

class Music():
    def __init__(self, 
                title: str,
                author: str,
                duration: int,
                cover: bytes,
                full_path: str):
        self.title = title
        self.author = author
        self.duration = duration # in seconds
        self.cover = cover # Path or cover datas
        self.full_path = full_path # file path

    @staticmethod
    def metadatas_from_file(file_path):
        """
        Creates and returns a Music instance 
        from a MP3 file.
        Args:
            file_path (str): full path to the
            MP3 file
        """
        # Load file datas
        audio = MP3(file_path, ID3=ID3)
        # Get title datas
        title_datas = audio.tags.get("TIT2", "Unknown")
        title = title_datas.text[0] if "TIT2" in audio.tags else "Unknown"
        # Get author datas
        author_datas = audio.tags.get("TPE1", "Unknown")
        author = author_datas.text[0] if "TPE1" in audio.tags else "Unknown"
        # Get file duration (seconds)
        duration = int(audio.info.length)

        # Get the cover
        cover = None
        # APIC = Attached PICture
        if "APIC" in audio.tags:
            apic = audio.tags["APIC:"]
            # Binaries of the image
            cover = apic.data

        return Music(title, author, duration, cover, file_path)
