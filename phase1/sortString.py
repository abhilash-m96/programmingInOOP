class SortString:

    def sort_string(self, string):
        arr = [char for char in string]

        #import pdb; pdb.set_trace()
        for i in range(len(string)):
            j = i + 1
            for j in range(len(string)):
                if arr[i] < arr[j]:
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp

        return arr

if __name__ == '__main__':
    str1 = SortString()
    print(str1.sort_string("klihefgadcba"))


