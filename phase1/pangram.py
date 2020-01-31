class Pangram:
    def __init__(self, string):
        self.string = string

    def remove_spaces(self, string):
        res = ""

        for char in string:
            if char != " ":
                res += char

        return res

    def sort_string(self, string):
        arr = [char for char in string]
        res = ""

        for i in range( len(arr) ):
            j = i + 1

            for j in range( len(arr) ):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]

        for char in arr:
            res += char
        
        return res

    def remove_spcl(self, string):
        res = ""

        for char in string:
            if ( ord(char) >= 97 and ord(char) <= 122) or (ord(char) <= 65 and ord(char) >= 90 ):
                res += char

        return res

    def check_pangram(self):
        str_wo_spaces = self.remove_spaces(self.string)

        str_sorted = self.sort_string(str_wo_spaces)

        # removing duplicates in the string
        str_uniq = "".join(set(str_sorted))
        str_alphabets = self.remove_spcl(str_uniq)

        if len(str_alphabets) == 26:
            return True
        else:
            return False

if __name__ == "__main__":
    string = input("Enter a sentence")
    obj = Pangram(string)
    
    pangram = obj.check_pangram()

    if pangram:
        print("Pangram")
    else:
        print("Not a pangram")
