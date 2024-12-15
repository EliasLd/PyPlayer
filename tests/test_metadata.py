import pytest
from src.music import Music

@pytest.mark.parametrize(
        "file_path, expected_title, expected_author, expected_duration", [
            ("tests/MP3_tests_files/Borderline.mp3", "Borderline", "Tame Impala", 237),
            ("tests/MP3_tests_files/HOODBYAIR.mp3", "HOODBYAIR", "Playboi Carti", 212),
            ("tests/MP3_tests_files/Pink + White.mp3", "Pink + White", "Frank Ocean", 184)
        ]
)
def test_mp3_metadata(file_path, expected_title,
                    expected_author,
                    expected_duration):
    
    test_music = Music.metadatas_from_file(file_path)

    assert test_music.title == expected_title
    assert test_music.author == expected_author
    assert test_music.duration == expected_duration