def camel_to_snake(variable_name):
     snake_case = ""
     for char in variable_name:
          if char.isupper():
               snake_case += "_" + char.lower()
          else:
               snake_case += char

     if snake_case.startswith("_"):
          snake_case = snake_case[1:]
     return snake_case


def main():
     camelCase = input("camelCase: ")
     snake_case = camel_to_snake(camelCase)
     print(f"snake_case: {snake_case}")


if __name__ == "__main__":
     main()
