import pytest
from PIL import Image
from io import BytesIO

from src.music import Music

@pytest.mark.parametrize(
        "file_path, expected_title, expected_author, \
            expected_duration, expected_cover_path", 
        [
            ("tests/MP3_tests_files/Borderline.mp3",
             "Borderline", 
             "Tame Impala",
             237, 
             "tests/images_tests_files/Tame Impala.jpg"),
            ("tests/MP3_tests_files/HOODBYAIR.mp3",
             "HOODBYAIR",
             "Playboi Carti",
             212,
             "tests/images_tests_files/Playboi Carti.jpg"),
            ("tests/MP3_tests_files/Pink + White.mp3",
             "Pink + White",
             "Frank Ocean",
             184,
             "tests/images_tests_files/Frank Ocean.jpg")
        ]
)
def test_mp3_metadata(file_path, expected_title,
                    expected_author,
                    expected_duration, 
                    expected_cover_path):
    """Compare metadatas of mp3 files
    to verify if the extraction works correctly.
    Args:
        file_path (str): path to the mp3 file
        expected_title (str): title of the music
        expected_author (str): author of the music
        expected_duration (int): duration in seconds
    """
    test_music = Music.metadatas_from_file(file_path)

    assert test_music.title == expected_title
    assert test_music.author == expected_author
    assert test_music.duration == expected_duration

    expected_cover = Image.open(expected_cover_path)
    # Open cover datas and convert from bytes
    # to Image object
    test_cover = Image.open(BytesIO(test_music.cover))
    
    assert images_are_equals(test_cover, expected_cover)

def images_are_equals(test_img, ref_img):
    """Compare two images to check if
    they are equals

    Args:
        test_img (str): path to the test image
        ref_img (str): path to the reference image
    """
    if test_img.size != ref_img.size:
        return False
    
    test_pixels = list(test_img.getdata())
    ref_pixels = list(ref_img.getdata())

    return test_pixels == ref_pixels