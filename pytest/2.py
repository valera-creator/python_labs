import pytest


# pytest -v pytest/2.py - для запуска
def test_value_error():
    with pytest.raises(TypeError):
        check_palindrome(3)


def test_empty():
    assert not check_palindrome('')


def test_small():
    assert not check_palindrome('ab')


def test_palindrome_register():
    assert check_palindrome('Alla')


def test_palindrome():
    assert check_palindrome('aba')


def test_not_palindrome():
    assert not check_palindrome('bear')


def check_palindrome(s):
    if not isinstance(s, str):
        raise TypeError

    if len(s) < 3:
        return False

    s = ''.join(s.split())
    return s.lower() == s[::-1].lower()
