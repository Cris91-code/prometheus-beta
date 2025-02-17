import pytest
from src.word_counter import count_words

def test_basic_word_count():
    assert count_words("Hello world") == 2
    assert count_words("One") == 1
    assert count_words("") == 0

def test_multiple_spaces():
    assert count_words("  Hello   world  ") == 2
    assert count_words("Spaces   between    words") == 4

def test_edge_cases():
    assert count_words(None) == 0
    assert count_words("   ") == 0
    assert count_words("\t\n") == 0

def test_punctuation_and_special_chars():
    assert count_words("Hello, world!") == 2
    assert count_words("Hyphenated-word test") == 2

def test_unicode_words():
    assert count_words("Café world") == 2
    assert count_words("こんにちは 世界") == 2  # Japanese words