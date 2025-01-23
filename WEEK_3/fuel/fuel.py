while True:
            try:
                user_input = input("Fraction: ")
                x, y = user_input.split("/")

                x = int(x)
                y = int(y)

                f = x / y

                if 0 <= f <= 1:
                       break

            except (ValueError, ZeroDivisionError):
                pass

p = round(f * 100)

if p <= 1:
       print(f"E")
elif p >= 99:
       print(f"F")
else:
       print(f"{p}%")
