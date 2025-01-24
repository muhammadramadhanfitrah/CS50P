class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{self.size*"🍪"}"

    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError("Cannot deposit: Exceeds jar capacity")
        self.size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Cannot withdraw: Not enough cookies in the jar")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError("Capacity must be at least 1")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size > self.capacity:
            raise ValueError("Size cannot exceed capacity")
        self._size = size


def main():
    jar = Jar()
    print(jar)

    n = int(input("Deposit: "))
    jar.deposit(n)
    print(jar)

    while True:
        print()
        response = input("Do you want to continue(y/n): ").lower()
        if response == "y" or response == "yes":
            print(f"{'SELECT'.center(30,'=')}")
            select = input("Deposit(1) or Withdraw(2): ")
            if select == "1":
                n = int(input("Deposit: "))
                jar.deposit(n)
                print(jar)
            elif select == "2":
                n = int(input("Withdraw: "))
                jar.withdraw(n)
                print(jar)
            else:
                print("Please select the correct option")
        elif response == "n" or response == "no":
            print(f"\n{'END OF PROGRAM'.center(30,'=')}")
            break
        else:
            print(f"Please select the correct option")
            continue


if __name__ == "__main__":
    main()
