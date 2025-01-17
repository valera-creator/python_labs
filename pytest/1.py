import pytest


# pytest -v pytest/1.py - для запуска
def test_value_error():
    with pytest.raises(ValueError):
        get_fact('s')


def test_zero():
    assert get_fact(0) == 1


def test_minus():
    assert get_fact(-2) == 'нет'


def test_correct():
    assert get_fact(5) == 120


def test_float():
    with pytest.raises(ValueError):
        get_fact('2.5')


def get_fact(n):
    if not isinstance(n, int):
        raise ValueError
    if n < 0:
        return 'нет'
    if n == 0:
        return 1
    mul = 1
    for i in range(2, n + 1):
        mul *= i
    return mul
