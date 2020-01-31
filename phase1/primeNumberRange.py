class PrimeNumberRange:
    def __init__(self, beginning, end):
        self.beginning = int(beginning)
        self.end = int(end)

    def is_prime(self, num):
        if num == 1:
            return True

        for i in range(2, num//2 +1):
            if num % i == 0:
                return False

        return True

    def prime_numbers(self):
        prime_numbers = []

        for i in range(self.beginning, self.end + 1):
            if self.is_prime(i):
                prime_numbers.append(i)

        return prime_numbers

if __name__ == "__main__":
    print("Enter range inclusive")
    beginning = input("Range beginning number")
    end = input("Range ending number")
    p1 = PrimeNumberRange(beginning, end)
    print(p1.prime_numbers())
