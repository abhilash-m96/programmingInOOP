# Convert lowercase to uppercase and uppercase to lowercase in a string

class CaseConversion:
    def convert_case(self):
        self.string = input("Enter a string")
        self.res = ""

        for char in self.string:
            if char.islower():
                self.res += char.upper()
            elif char.isupper():
                self.res += char.lower()
            else:
                self.char += char

        return self.res


if __name__ == "__main__":
    obj1 = CaseConversion()
    print(obj1.convert_case())
