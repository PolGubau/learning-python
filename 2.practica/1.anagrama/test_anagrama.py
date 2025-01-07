# test_anagrama.py
from isAnagrama import isAnagrama

def test_anagramas():
    assert isAnagrama("roma", "amor")  # Simple case
    assert isAnagrama("Listen", "Silent")  # Case insensitive
    assert isAnagrama("a gentleman", "elegant man")  # Handles spaces

def test_no_anagramas():
    assert not isAnagrama("hello", "world")  # Different words
    assert not isAnagrama("test", "tests")  # Different lengths
    assert not isAnagrama("anagram", "nagaramm")  # Extra character
