import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
argv1 = ["-f", "--font"]

if len(sys.argv) < 2:
    isRandomFont = True
elif len(sys.argv) > 2 and (sys.argv[1] in argv1):
    isRandomFont = False
else:
    sys.exit("Invalid usage")

# Get a list of available font
availableFont = figlet.getFonts()

if isRandomFont == False:
    try:
        figlet.setFont(font = sys.argv[2])
    except:
        sys.exit("Invalid usage")
else:
    font = random.choice(availableFont)

user_input = input("Input: ")

print(f"Output: ")
print(f"{figlet.renderText(user_input)}")
