import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if youtube_link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([\w]+)\"></iframe>", s):
        return f"https://youtu.be/{youtube_link.group(2)}"
    else:
        return None


if __name__ == "__main__":
    main()
