import sys


def main():
    check_command_line_argv()
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    count_lines = 0

    for line in lines:
        if is_blank_or_comment(line) == False:
            count_lines += 1

    if count_lines < 2:
        print(f"There are {count_lines} line in {sys.argv[1]}")
    else:
        print(f"There are {count_lines} lines in {sys.argv[1]}")


def is_blank_or_comment(line):
    stripped_line = line.strip()
    return not stripped_line or stripped_line.startswith("#")


def check_command_line_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
