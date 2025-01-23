import emoji


def convert_emoji(text):
    emoticons = emoji.emojize(text, language="alias")
    return emoticons


def main():
    user_input = input("Enter text: ")
    converted_emoji = convert_emoji(user_input)
    print(f"{converted_emoji}")


if __name__ == "__main__":
    main()
