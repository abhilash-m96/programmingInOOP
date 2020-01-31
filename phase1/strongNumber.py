class StrongNumber:
    def __init__(self, num):
        self.num = num

    def fact(self, num):
        if num == 1:
            return num
        elif num == 0:
            return 1 
        else:
            return num * self.fact(num -1)

    def is_strong(self):
        res = 0

        for digit in self.num:
            res += self.fact(int(digit))

        if res == int(self.num):
            return True
        else:
            return False

if __name__ == "__main__":
    num = input("Enter a number")
    s1 = StrongNumber(num)

    if s1.is_strong():
        print("Strong Number")
    else:
        print("Not a strong number")
