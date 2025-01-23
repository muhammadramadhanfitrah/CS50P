from twttr import shorten


def main():
    test_upper_and_lower_case()
    test_numbers()
    test_punctuation()


def test_upper_and_lower_case():
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwITtEr") == "TwTtr"


def test_numbers():
    assert shorten("12345") == "12345"


def test_punctuation():
    assert shorten("!?.,:;")


if __name__ == "__main__":
    main()
