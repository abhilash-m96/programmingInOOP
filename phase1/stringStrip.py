class StringStrip:
    def get_input(self):
        self.string = input("Enter a string")

        return self.string

    def cust_strip(self, string):
        self.string = string
        self.start = self.get_first_index(self.string)
        self.end = self.get_last_index(self.string[::-1])
        self.res = ''

        #print(self.start, self.end)

        for i in range( self.start, self.end + 1 ):
            self.res += self.string[i]

        return self.res

    def get_first_index(self, string):
        self.index = 0

        for i in range( len(self.string) ):
            if self.string[i] != " ":
                self.index = i

                return self.index

    def get_last_index(self, string):
        self.index = 0

        for i in range(len(string)-1, 0, -1):
            if self.string[i] != " ":
                self.index = i

                return self.index


if __name__ == "__main__":
    s1 = StringStrip()
    string = s1.get_input()

    print(s1.cust_strip(string))


