"""
Perfect Number: A number is said to be a perfect number, if the sum of square of its proper-divisors is equal to the number itself.
"""

class PerfectNumber:
    def __init__(self, num):
        self.num = int(num)

    def is_perfect(self):
        res = 0

        for i in range(2, self.num):
            if self.num % i == 1:
                res += i**2

        if res == self.num:
            return True
        else:
            return False

if __name__ == "__main__":
    import pdb; pdb.set_trace()
    num = input("Enter a number")
    p1 = PerfectNumber(num)
    if p1.is_perfect():
        print("Perfect Number")
    else:
        print("Not a perfect number")

