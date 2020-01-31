"""
Happynumber: A number is said to be a HappyNumber when the number is replaced by sum of square of its digits in a loop until the sum of square of digits yields a single digit. Once we get single digit then if the single digit is 1 then it is a happynumber else not.
"""

class HappyNumber:
    def __init__(self, num):
        self.num = num

    def get_sum_of_squares(self, number):
        res = 0

        for digit in number:
            res += int(digit) ** 2

        res = str(res)

        if len(res) != 1:
            return self.get_sum_of_squares(res)
        else:
            return int(res)

    def check_if_happy(self):
        res = self.get_sum_of_squares(self.num)

        if res == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    num = input("Enter a number to check if it is happy or not xP")
    h1 = HappyNumber(num)

    if h1.check_if_happy():
        print("Happy Number")
    else:
        print("Not an happy number")
