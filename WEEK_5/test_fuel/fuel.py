def main():
    try:
        frac = input("Fraction: ")
        pct = convert(frac)
        print(gauge(pct))
    except ValueError:
        print("Error: Invalid fraction.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")


def convert(fraction):
    x, y = fraction.split("/")
    x, y = int(x), int(y)

    result = x / y

    if y == 0:
        raise ZeroDivisionError
    elif result > 1:
        raise ValueError

    return int(result * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 1 < percentage < 99:
        return f"{percentage}%"
    elif percentage >= 99:
        return "F"


if __name__ == "__main__":
    main()
