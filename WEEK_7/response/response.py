from validator_collection import validators


def main():
    print(email_validator(input("What's your email address? ")))


def email_validator(email_address):
    try:
        validators.email(email_address)
        return "Valid"
    except Exception:
        return "Invalid"


if __name__ == "__main__":
    main()
