def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    user_input = input("Enter a text: ")
    converted_text = convert(user_input)
    print(f"Converted text: {converted_text}")


main()
