import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^[\d]+\.[\d]+\.[\d]+\.[\d]+$", ip):
        octets = ip.split(".")
        for number in octets:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
