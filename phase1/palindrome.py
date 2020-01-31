class Palindrome:
    def __init__(self, inp):
        self.inp = inp

    def check_palindrome(self):
        reverse_inp = ""

        for i in range(len(self.inp) - 1, -1, -1 ):
            reverse_inp += self.inp[i]

        print(self.inp, reverse_inp)
        if self.inp == reverse_inp:
            print("Match! It's a palindrome")
        else:
            print("Not a palindrome")

if __name__ == "__main__":
    inp  = input("Enter input")
    p1 = Palindrome(inp)
    p1.check_palindrome()
