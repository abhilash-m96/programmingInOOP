"""
Armstrong number: If the sum of cube of digits of a number is equal to the number itself then the number is said to be a Armstrong number
"""

class Armstrong:
    def __init__(self, num):
        self.num = num

    def check_armstrong(self):
        res = 0

        for digit in self.num:
            res += int(digit) ** 3

        if int(self.num) ==  res:
            return True
        else:
            return False

if __name__ == "__main__":
    num = input("Enter num to check if it is Armstrong number")
    a1 = Armstrong(num)
    if(a1.check_armstrong()):
        print("Armstrong Number")
    else:
        print("Not an Armstrong number")

