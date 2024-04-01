"""Dictionary tests for functions in EX05."""

__author__ = "730649327"


from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert() -> None:
    """Test basic use case for invert function."""
    t: dict[str, str] = {"a": "b"}
    assert invert(t) == {"b": "a"}


def test_invert_2() -> None:
    """Test basic use case 2 for invert function."""
    t: dict[str, str] = {"1": "2"}
    assert invert(t) == {"2": "1"}


def test_invert_3() -> None:
    """Test basic edge case for invert function."""
    t: dict[str, str] = {"aaaaaaaaaaaaaaaaaaab": "a", "aaaaaaaaaaaaaaaab": "c"}
    assert invert(t) == {"a": "aaaaaaaaaaaaaaaaaaab", "c": "aaaaaaaaaaaaaaaab"}


def test_favorite_color() -> None:
    """Test basic use case for favorite color function."""
    t: dict[str, str] = {"John": "red", "John1": "blue", "John2": "red"}
    assert favorite_color(t) == "red"
    

def test_favorite_color_2() -> None:
    """Test basic use case 2 for favorite color function."""
    t: dict[str, str] = {"Amy": "green", "Amy2": "green", "Amy3": "green"}
    assert favorite_color(t) == "green"


def test_favorite_color_3() -> None:
    """Test basic edge case for favorite color function."""
    t: dict[str, str] = {"John": "red", "John": "red", "John1": "blue"}
    assert favorite_color(t) == "red"


def test_count() -> None:
    """Test basic use case for count function."""
    t: list[str] = ["red", "red", "blue"]
    assert count(t) == {"red": 2, "blue": 1}
    

def test_count_2() -> None:
    """Test basic use case 2 for count function."""
    t: list[str] = ["apple", "orange", "orange"]
    assert count(t) == {"apple": 1, "orange": 2}


def test_count_3() -> None:
    """Test basic edge case for count function."""
    t: list[str] = []
    assert count(t) == {}


def test_alphabetizer() -> None:
    """Test basic use case for alphabetizer function."""
    t: list[str] = ["cat", "dog", "fish"]
    assert alphabetizer(t) == {'c': ['cat'], 'd': ['dog'], 'f': 'fish'}


def test_alphabetizer_2() -> None:
    """Test basic use case 2 for alphabetizer function."""
    t: list[str] = ["apple", "apricot", "banana", "blueberry"]
    assert alphabetizer(t) == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}


def test_alphabetizer_3() -> None:
    """Test basic edge case for alphabetizer function."""
    t: list[str] = []
    assert alphabetizer(t) == {}


def test_update_attendance() -> None:
    """Test basic use case for update attendance function."""
    t: dict[str, list[str]] = {"Monday": ["John", "John1"], "Tuesday": ["John2"]}
    dotw = "Monday"
    name = "Jessie"
    assert update_attendance(t, dotw, name) == {'Monday': ["John", "John1", "Jessie"], 'Tuesday': ["John2"]}


def test_update_attendance_2() -> None:
    """Test basic use case 2 for update attendance function."""
    t: dict[str, list[str]] = {"Monday": ["Amy", "John"], "Tuesday": ["John"]}
    dotw = "Tuesday"
    name = "Amy"
    assert update_attendance(t, dotw, name) == {'Monday': ["John", "John1", "Jessie"], 'Tuesday': ["John2"]}


def test_update_attendance_3() -> None:
    """Test basic edge case for update attendance function."""
    t: dict[str, list[str]] = {"Monday": ["John", "John1"], "Tuesday": ["John2"]}
    dotw = "Monday"
    name = "John"
    assert update_attendance(t, dotw, name) == {"Monday": ["John", "John1"], "Tuesday": ["John2"]}