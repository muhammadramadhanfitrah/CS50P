def calculator_expression(expression):
     x, y, z = expression.split(" ")

     x = int(x)
     z = int(z)

     if y == "+":
          return x + z
     elif y == "-":
          return x - z
     elif y == "*":
          return x * z
     elif y == "/" and z != 0:
          return x / z
     else:
          print("error")


def main():
     user_input = input("Expression: ")
     result = calculator_expression(user_input)
     print(f"{result:.1f}")


if __name__ == "__main__":
     main()
