import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

# B-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_unique_sorted():
    assert unique_sorted([3, 1, 2, 2, 3]) == [1, 2, 3]
    assert unique_sorted([5, 5, 5]) == [5]
    assert unique_sorted([]) == []
    assert unique_sorted([-1, 0, 2, 2]) == [-1, 0, 2]


def test_count_words():
    text = "Hello hello WORLD world"
    expected = {"hello": 2, "world": 2}
    assert count_words(text) == expected

    text2 = "hi hi hi"
    expected2 = {"hi": 3}
    assert count_words(text2) == expected2

    text3 = ""
    expected3 = {}
    assert count_words(text3) == expected3


def test_merge_dicts():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 20, "c": 3}
    merged = merge_dicts(d1, d2)
    assert merged == {"a": 1, "b": 20, "c": 3}

    assert d1 == {"a": 1, "b": 2}
    assert d2 == {"b": 20, "c": 3}


def test_find_max_pair():
    assert find_max_pair([1, 3, 2, 3, 3]) == (3, 3)
    assert find_max_pair([-5, -1, -3, -1]) == (-1, 2)


def test_flatten():
    assert flatten([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten([[1, [2]], [3]]) == [1, [2], 3]
    assert flatten([[]]) == []
    assert flatten([]) == []


def test_write_and_read_file(tmp_path):
    path = tmp_path / "test.txt"
    text = "Hello, world!"

    n = write_file(str(path), text)
    assert n == len(text)

    content = read_file(str(path))
    assert content == text


def test_safe_get():
    d = {"x": 1}
    assert safe_get(d, "x") == 1
    assert safe_get(d, "y") is None
    assert safe_get(d, "y", default=0) == 0


def test_top_n():
    nums = [5, 1, 3, 5, 2]
    assert top_n(nums, 1) == [5]
    assert top_n(nums, 3) == [5, 5, 3]


def test_chunk_list():
    lst = [1, 2, 3, 4, 5]
    assert chunk_list(lst, 2) == [[1, 2], [3, 4], [5]]
    assert chunk_list(lst, 1) == [[1], [2], [3], [4], [5]]
    assert chunk_list(lst, 10) == [[1, 2, 3, 4, 5]]

# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
