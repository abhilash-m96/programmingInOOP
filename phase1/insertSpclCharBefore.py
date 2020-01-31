# Insert a spcl. charatcter "*" before "a" or "A" in a string

class InsertSpcl:

    def insert_star_before_a_A(self):

        self.string = input("Enter a string")
        self.res = ""

        for char in self.string:
            if char != "a" and char != "A":
                self.res += char
            else:
                self.res += "*" + char

        return self.res

if __name__ == "__main__":
    obj1 = InsertSpcl()
    print(obj1.insert_star_before_a_A())
