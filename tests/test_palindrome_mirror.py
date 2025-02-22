import pytest
from src.palindrome_mirror import create_palindrome_mirror

def test_basic_string_palindrome_mirror():
    assert create_palindrome_mirror("hello") == "helloolleh"

def test_empty_string_palindrome_mirror():
    assert create_palindrome_mirror("") == ""

def test_number_string_palindrome_mirror():
    assert create_palindrome_mirror("123") == "123321"

def test_special_characters_palindrome_mirror():
    assert create_palindrome_mirror("hi!@#") == "hi!@#@#!ih"

def test_spaces_palindrome_mirror():
    assert create_palindrome_mirror("hello world") == "hello worlddlrow olleh"

def test_mixed_characters_palindrome_mirror():
    assert create_palindrome_mirror("a1b!c ") == "a1b!c  c!b1a"

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a string"):
        create_palindrome_mirror(123)
        create_palindrome_mirror(None)
        create_palindrome_mirror(["hello"])