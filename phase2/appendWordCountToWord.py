class AppendWordCount:
    def __init__(self, string):
        self.string = string

    def append_count(self):
        words = self.string.split(" ")

        res = ""
        for word in words:
            if word != "":
                res += word + str(len(word)) + " "
            else:
                res += " "

        return res

if __name__ == "__main__":
    string = input("Enter a sentence \n")
    a1 = AppendWordCount(string)
    print(a1.append_count())
