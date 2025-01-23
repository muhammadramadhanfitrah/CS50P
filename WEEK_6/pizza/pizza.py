import sys
import csv
from tabulate import tabulate


def main():
    check_command_line_argv()
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            table = tabulate(reader, headers="firstrow", tablefmt="grid")
            print(table)
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_command_line_argv():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
