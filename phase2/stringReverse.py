class StringReverse:
    def __init__(self, string):
        self.string = string

    def cust_reverse(self):
        res = ""

        for i in range( len(self.string)-1, -1, -1 ):
            res += self.string[i]

        return res

if __name__ == "__main__":
    string = input("Enter a string")
    s1 = StringReverse(string)
    print(s1.cust_reverse())

