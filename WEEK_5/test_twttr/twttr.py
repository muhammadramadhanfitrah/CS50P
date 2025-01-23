def main():
    user_input = input("Input: ")

    message_without_vowels = shorten(user_input)

    print(f"Output: {message_without_vowels}")


def shorten(word):
    vowels = ["a", "i", "u", "e", "o"]
    result = ""
    for letter in word:
         if letter.lower() not in vowels:
              result += letter

    return result


if __name__ == "__main__":
    main()
