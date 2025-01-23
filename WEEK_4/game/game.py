import random

while True:
    try:
        level = int(input("Level: "))
        random_value = random.randint(1, level)
        while True:
            guess = int(input("Guess: "))
            if guess < random_value:
                print(f"Too small!")
            elif guess > random_value:
                print(f"Too large!")
            else:
                print(f"Just right!")
                raise EOFError
    except ValueError:
        pass
    except EOFError:
        break
