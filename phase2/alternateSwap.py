class AlternateSwap:
    def __init__(self, string):
        self.string = string

    def alternate_swap(self):
        words = self.string.split(" ")

        res = ""

        for i in range(0, len(words)//2, 2):
            words[i], words[len(words) - 1 -i] = words[len(words) -1 -i], words[i]

        for word in words:
            res += word + " "

        return res

if __name__ == "__main__":
    inp = input("Enter a sentence \n")
    a1 = AlternateSwap(inp)
    print(a1.alternate_swap())

