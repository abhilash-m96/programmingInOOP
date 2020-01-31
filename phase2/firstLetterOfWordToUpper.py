class FirstLetterUpperCase:
    def __init__(self, sentence):
        self.sentence = sentence

    def perform(self):
        words = self.sentence.split()
        res = ''

        for i in range(len(words)):
            if len(words[i]) > 0 and words[i] != ' ':
                words[i] = words[i][0].upper() + words[i][1:]

        for word in words:
            res += word + " "

        return res

if __name__ == "__main__":
    sentence = input("Enter a sentence \n")
    f1 = FirstLetterUpperCase(sentence)
    print(f1.perform())

