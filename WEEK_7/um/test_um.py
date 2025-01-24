import pytest
from um import count


def test_um_counter():
    assert count("um") == 1
    assert count("Um, thank you") == 1
    assert count("um um Um") == 3
    assert count("yummy") == 0
    assert count("um, my name is umar, um yes") == 2


if __name__ == "__main__":
    test_um_counter()
