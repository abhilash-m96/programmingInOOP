class StringManipulation:
    def __init__(self, string):
        self.string = string

    def perform(self):
        words = self.string.split(" ")

        res = ""

        for i in range(0, len(words)//2):
            res += words[i] + words[len(words) -i -1] + str( len(words[i] + words[len(words) -i -1])  ) + " "

        if len(words) % 2 != 0:
            res += words[len(words)//2] + str(len( words[len(words)//2] ))
        return res

if __name__ == "__main__":
    inp = input("Enter a string \n")
    s1 = StringManipulation(inp)

    print(s1.perform())


