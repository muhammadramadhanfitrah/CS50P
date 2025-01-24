from datetime import date
import reWE
import sys
import inflect


p = inflect.engine()


def main():
    birth = input("Date of birth (YYYY-MM-DD): ")
    try:
        year, month, day = validate_birth(birth)
    except:
        sys.exit("Invalid Date")

    today = date.today()
    date_of_birth = date(year, month, day)

    days_difference = today - date_of_birth
    print(minutes_converter(days_difference.days))


def validate_birth(birth):
    if match := re.search(r"^[0-9]{4}-((0[1-9]|1[0-2]))-((0[1-9]|1[0-9]|2[0-9]|3[0-1]))$", birth):
        year, month, day = birth.split("-")
        return int(year), int(month), int(day)


def minutes_converter(days):
    minutes = days * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()
