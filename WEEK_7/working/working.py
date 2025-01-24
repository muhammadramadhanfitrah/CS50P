import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r"(0?[1-9]|1[0-2]):?([0-5][0-9])? (AM|PM)"
    try:
        if matches := re.fullmatch(rf"^{regex} to {regex}$", s):
            from_hour = matches.group(1)
            from_minute = matches.group(2) or "00"
            from_period = matches.group(3)

            to_hour = matches.group(4)
            to_minute = matches.group(5) or "00"
            to_period = matches.group(6)

            from_time = standardize(from_hour, from_minute, from_period)
            to_time = standardize(to_hour, to_minute, to_period)

            return f"{from_time} to {to_time}"
        else:
            raise ValueError
    except ValueError:
        sys.exit("ValueError")


def standardize(hour, minute, period):
    if period == "AM":
        if hour == "12":
            converted_hour = "00"
        else:
            converted_hour = f"{int(hour):02}"
    elif period == "PM":
        if hour == "12":
            converted_hour = "12"
        else:
            converted_hour = f"{int(hour) + 12}"

    converted_minute = f"{int(minute):02}"
    return f"{converted_hour}:{converted_minute}"


if __name__ == "__main__":
    main()
