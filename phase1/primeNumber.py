class PrimeNumber:
    def __init__(self, num):
        self.num = int(num)

    def is_prime(self):
        if self.num == 1:
            return True

        for i in range(2, self.num//2 + 1):
            if self.num % i == 0:
                return False

        return True

if __name__ == "__main__":
    num = input("Enter a number")
    p1 = PrimeNumber(num)

    if p1.is_prime():
        print("Prime Number")
    else:
        print("Not a prime number")

