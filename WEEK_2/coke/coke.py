def main():
     amount_due = 50

     while amount_due > 0:
          print(f"Amount Due: {amount_due}")
          coin = int(input("Insert coint: "))
          if coin in [50, 25, 10, 5]:
               amount_due -= coin
          else:
               continue

     change_owed = abs(amount_due)
     print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
     main()
