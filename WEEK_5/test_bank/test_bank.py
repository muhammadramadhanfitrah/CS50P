from bank import value


def main():
    test_return_zero()
    est_return_twenty()
    test_return_one_hundred()


def test_return_zero():
    assert value("hello riri") == 0
    assert value("HELLO ROCKY") == 0


def test_return_twenty():
    assert value("hi riri") == 20
    assert value("HI ROCKY") == 20


def test_return_one_hundred():
    assert value("wassup riri") == 100
    assert value("WASSUP ROCKY") == 100


if __name__ == "__main__":
    main()
