import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1], sys.argv[2])


def clean(before, after):
    try:
        with open(before) as input_file:
            reader = csv.DictReader(input_file)
            with open(after, "w") as output_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(output_file, fieldnames = fieldnames)
                writer.writeheader()
                for student in reader:
                    last, first = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first, "last": last, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == "__main__":
    main()
