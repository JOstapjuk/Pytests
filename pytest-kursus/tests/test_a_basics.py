import math
import pytest
from src.a_basics import (
    add, sub, mul, div, sum_list, is_even, factorial, reverse_string,
    is_palindrome, to_title_case, clamp, median, unique_letters, safe_int, nth_root
)

def test_add_basic():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_sub_basic():
    """Test subtraction function."""
    assert sub(10, 7) == 3 #FAIL
    assert sub(5, 3) == 2 
    assert sub(0, 5) == -5

def test_mul():
    """Test multiplication function."""
    assert mul(3, 4) == 12
    assert mul(-2, 5) == -10
    assert mul(0, 100) == 0

def test_div():
    """Test division function."""
    assert div(10, 2) == 5
    assert div(-9, 3) == -3

def test_sum_list():
    """Test list summation function."""
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([]) == 0
    assert sum_list([-1, -2, -3]) == -6

def test_is_even():
    """Test even number check."""
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True

def test_factorial():
    """Test factorial function."""
    assert factorial(0) == 1
    assert factorial(5) == 120

def test_reverse_string():
    """Test string reversing."""
    assert reverse_string("abc") == "cba"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"

def test_is_palindrome():
    """Test palindrome check."""
    assert is_palindrome("aba") is True
    assert is_palindrome("abba") is True
    assert is_palindrome("AbBa") is True # FAILS
    assert is_palindrome("A man a plan a canal Panama") is True
    assert is_palindrome("hello") is False

def test_to_title_case():
    """Test title case conversion."""
    assert to_title_case("hello world") == "Hello World"
    assert to_title_case("multiple words here") == "Multiple Words Here"

def test_clamp():
    """Test value clamping."""
    assert clamp(5, 0, 10) == 5
    assert clamp(-1, 0, 10) == 0
    assert clamp(15, 0, 10) == 10

def test_median():
    """Test median calculation."""
    assert median([1, 3, 2]) == 2
    assert median([1, 2, 3, 4]) == 2.5
    assert median([7]) == 7

def test_unique_letters():
    """Test unique letter extraction."""
    assert unique_letters("Hello!") == {"h", "e", "l", "o"}
    assert unique_letters("123") == set()
    assert unique_letters("AaBb") == {"a", "b"}

def test_safe_int():
    """Test safe int conversion."""
    assert safe_int("42") == 42
    assert safe_int("not a number", default=-1) == -1
    assert safe_int("3.14", default=0) == 0  # float string / ValueError

def test_nth_root():
    """Test nth root calculation."""
    assert nth_root(27, 3) == 3
    assert math.isclose(nth_root(16, 2), 4)
