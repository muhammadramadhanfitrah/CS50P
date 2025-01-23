def main():
     user_input = input("Input: ")
     vowels = ["a", "i", "u", "e", "o"]

     print("Output: ", end="")

     for letter in user_input:
          if letter.lower() not in vowels:
               print(letter, end="")

     print()


if __name__ == "__main__":
     main()
