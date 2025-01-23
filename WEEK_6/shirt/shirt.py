from PIL import Image, ImageOps
import sys
import os


def main():
    check_arguments()
    check_extensions()
    try:
        edit_photo(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_arguments():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


def check_extensions():
    supported_file = [".jpg", ".jpeg", ".png"]
    input_file = os.path.splitext(sys.argv[1])
    output_file = os.path.splitext(sys.argv[2])

    if input_file[1].lower() not in supported_file:
        sys.exit("Invalid input")
    elif output_file[1].lower() not in supported_file:
        sys.exit("Invalid output")

    if input_file[1] != output_file[1]:
        sys.exit("Input and output have different extensions")


def edit_photo(input_file, output_file):
    shirt = Image.open("shirt.png")
    with Image.open(input_file) as img:
        img_cropped = ImageOps.fit(img, shirt.size)
        img_cropped.paste(shirt, mask = shirt)
        img_cropped.save(output_file)


if __name__ == "__main__":
    main()
