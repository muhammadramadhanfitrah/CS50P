import random


def main():
    remaining_questions = 10
    remaining_attempts = 3
    score = 0
    level = get_level()

    while remaining_questions > 0:
        if remaining_attempts == 3:
            X, Y = generate_integer(level)

        solution = X + Y

        try:
            answer = int(input(f"{X} + {Y} = "))
            if answer == solution:
                score += 1
                remaining_questions -= 1
                remaining_attempts = 3
                continue
            else:
                raise ValueError

        except ValueError:
            print(f"EEE")
            remaining_attempts -= 1

        if remaining_attempts == 0:
            print(f"{X} + {Y} = {solution}")
            remaining_attempts = 3
            remaining_questions -= 1
            continue

    print(f"Score: {score}")


def get_level():
    valid_levels = [1, 2, 3]
    print(f"Select Level (1, 2, or 3)")

    while True:
        try:
            level = int(input("Level: "))
            if level in valid_levels:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()
