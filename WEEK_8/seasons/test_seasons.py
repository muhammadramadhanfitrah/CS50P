from seasons import minutes_converter
import pytest


def test_minutes_converter():
    assert minutes_converter(1) == "One thousand, four hundred forty minutes"
    assert minutes_converter(365) == "Five hundred twenty-five thousand, six hundred minutes"


if __name__ == "__main__":
    test_minutes_converter()
