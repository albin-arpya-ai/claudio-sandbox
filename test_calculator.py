from calculator import add, multiply


def test_add():
    assert add(2, 2) == 4


def test_add_with_negative():
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(3, 4) == 12
