# Append the alternative words and also the length after appending the words

class AppendOpertaion:
    def __init__(self, sentence):
        self.sentence = sentence


    def perform(self):
        words = self.sentence.split()
        res = ""

        for i in range(len(words)//2):
            modedword = words[i] + words[len(words) - i - 1]
            res += modedword + str(len(modedword)) + " "

        if len(words) % 2 != 0:
            res += words[len(words)//2] + str(len(words[len(words)//2]))


        return res

if __name__ == "__main__":
    sentence = input("Enter a sentence \n")
    a1 = AppendOpertaion(sentence)
    print(a1.perform())


