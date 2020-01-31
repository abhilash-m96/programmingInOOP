from stringReverse import StringReverse

class WordReverse:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        res = ""

        words = self.string.split(" ")

        for word in words:
            if word != " ":
                s1 = StringReverse(word)
                res += s1.cust_reverse() + " "
            else:
                res += word

        return res

if __name__ == "__main__":
    string = input("Enter a sentence \n")
    w1 = WordReverse(string)
    print(w1.reverse())
