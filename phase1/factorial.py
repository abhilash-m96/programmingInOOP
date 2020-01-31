class Factorial:
    def __init__(self, num):
        self.num = int(num)

    def get_factorial(self):
        fact = 1

        for i in range(self.num, 0, -1):
            fact *= i

        print(fact)

    def recursion_factorial(self, num):
        num = int(num)

        if num == 1:
            return num
        elif num == 0:
            return 1
        else:
            return num * self.recursion_factorial(num -1)

if __name__ == '__main__':
    num = input("Enter a number")
    f1 = Factorial(num)
    f1.get_factorial()
    print(f1.recursion_factorial(num))

