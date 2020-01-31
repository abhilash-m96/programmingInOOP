import multiprocessing as mp

class DiffCharCount:

    def __init__(self, string):
        self.string = string
        print(f"Sentence is \n{self.string}")
        p1 = mp.Process(target=self.num_count, args=(string,))
        p2 = mp.Process(target=self.vowel_and_cons_count, args=(string,))
        p3 = mp.Process(target=self.spcl_count, args=(string,))

        p1.start()
        p2.start()
        p3.start()

        p1.join()
        p2.join()
        p3.join()

    def num_count(self, string):
        count = 0

        for i in string:
            if ord(i) >= 48 and ord(i) <= 57:
                count += 1

        print(f"Numbers count is {count}")

    def vowel_and_cons_count(self, string):
        count = 0
        vowel_count = 0
        conso_count = 0
        vowels = ["a", "e", "i", "o", "u"]

        for i in string:
            if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
                count += 1

                if i in vowels:
                    vowel_count += 1
                else:
                    conso_count += 1

        print(f"Alphabets count is {count}")
        print(f"Vowels count is {vowel_count}")
        print(f"Consonants count is {conso_count}")

    def spcl_count(self, string):
        count = 0

        for i in string:
            if (ord(i) not in range(48, 58)) and (ord(i) not in range(65, 91)) and (ord(i) not in range(97,123)):
                count += 1

        print(f"Special characters count is {count}")

if __name__ == '__main__':
   string = input("Enter the sentence")
   obj = DiffCharCount(string)
