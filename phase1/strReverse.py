class StrReverse:
    def rev_str1(string):
        length = len(string)

        res = ""
        for i in reversed(range(length)):
            res += string[i]

        return res

    def rev_str2(string):
        length = len(string)
        arr = [char for char in string]

        result = ""

        for i in range(length//2):
            temp = arr[i]
            arr[i] = arr[length - 1 - i]
            arr[length - 1 -i] = temp

        for char in arr:
            result += char

        return result


if __name__ == '__main__':
    print(StrReverse.rev_str1("My name is abhilash"))
    print(StrReverse.rev_str2("My name is abhilash"))
