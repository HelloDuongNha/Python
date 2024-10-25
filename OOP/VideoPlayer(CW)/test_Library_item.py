import pytest
from Resource_Library_Item import LibraryItem

def test_library_item():
    item = LibraryItem(1, "Movie", "Director", 4, 100, "path/to/image.jpg")
    assert item.id == 1
    assert item.name == "Movie"
    assert item.director == "Director"
    assert item.rating == 4
    assert item.play_count == 100
    assert item.image_path == "path/to/image.jpg"

def test_invalid_id():
    with pytest.raises(ValueError):
        LibraryItem("a", "Movie", "Director", 4, 100)

def test_negative_id():
    with pytest.raises(ValueError):
        LibraryItem(-1, "Movie", "Director", 4, 100)

def test_empty_name():
    with pytest.raises(ValueError):
        LibraryItem(1, "", "Director", 4, 100)

def test_empty_director():
    with pytest.raises(ValueError):
        LibraryItem(1, "Movie", "", 4, 100)

def test_invalid_rating():
    with pytest.raises(ValueError):
        LibraryItem(1, "Movie", "Director", "five", 100)

def test_rating_out_of_range():
    with pytest.raises(ValueError):
        LibraryItem(1, "Movie", "Director", 6, 100)

def test_negative_play_count():
    with pytest.raises(ValueError):
        LibraryItem(1, "Movie", "Director", 4, -10)

def test_empty_image_path():
    item = LibraryItem(1, "Movie", "Director", 4, 100)
    with pytest.raises(ValueError):
        item.image_path = ""

def test_save_item():
    item = LibraryItem(1, "Movie", "Director", 4, 100)
    assert item.save_item() == "1,Movie,Director,****"

def test_info():
    item = LibraryItem(1, "Movie", "Director", 4, 100)
    assert item.info() == "Movie - Director - ****"

def test_stars():
    item = LibraryItem(1, "Movie", "Director", 4, 100)
    assert item.stars() == "****"
