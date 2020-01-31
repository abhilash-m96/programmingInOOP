"""
Happynumber: A number is said to be a HappyNumber when the number is replaced by sum of square of its digits in a loop until the sum of square of digits yields a single digit. Once we get single digit then if the single digit is 1 then it is a happynumber else not.
"""

class HappyNumber:
    def __init__(self, begin, end):
        self.begin = int(begin)
        self.end = int(end)

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
        happy_numbers = []

        for num in range(self.begin, self.end + 1):
            res = self.get_sum_of_squares(str(num))

            if res == 1:
                happy_numbers.append(num)

        return happy_numbers

if __name__ == "__main__":
    begin = input("Enter range inclusive: from: \n")
    end = input("Enter range: to \n")
    h1 = HappyNumber(begin, end)

    print(h1.check_if_happy())
