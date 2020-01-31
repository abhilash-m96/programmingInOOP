class NoOfWords:
    def string_input(self):
        self.string = input("Enter a sentence")
        return self.string

    def count_words(self, string):
        # White spaces on either sides if any will be removed
        self.string = string.strip()
        print(self.string)
        word_count = 0

        for i in range(len(self.string) -1 ):
            if string[i] != " " and string[i+1] == " ":
                word_count += 1

        return word_count + 1

if __name__ == "__main__":
    obj = NoOfWords()
    string = obj.string_input()
    print(obj.count_words(string))


