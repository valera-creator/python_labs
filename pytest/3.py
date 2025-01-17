import pytest


# pytest -v pytest/3.py - для запуска
def test_value_error():
    with pytest.raises(TypeError):
        get_cnt_equal_symbols(3)


def test_empty():
    assert get_cnt_equal_symbols('') == 0


def test_not_equal():
    assert get_cnt_equal_symbols('abcd') == 0


def test_two_equal():
    assert get_cnt_equal_symbols('Alla') == 2


def test_one_equal():
    assert get_cnt_equal_symbols('aba') == 1


def get_cnt_equal_symbols(s):
    if not isinstance(s, str):
        raise TypeError

    if not s:
        return 0

    s = ''.join(s.split()).lower()  # не учитываю регистр
    return sum(1 for elem in set(s) if s.count(elem) > 1)
