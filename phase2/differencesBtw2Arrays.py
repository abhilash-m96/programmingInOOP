# Both A-B and B-A, i,e. Those elements of A not in B and those elements of B not in A

class ArrayDifference:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def difference(self):
        res1 = [] # A - B
        res2 = [] # B - A

        for item in self.arr1:
            if item not in self.arr2:
                res1.append(item)

        for item in self.arr2:
            if item not in self.arr1:
                res2.append(item)

        return res1, res2

if __name__ == "__main__":
    arr1 = [ x for x in input("Enter items of first array seperated by space \n").split() ]
    arr2 = [ x for x in input("Enter items of second array seperated by space \n").split() ]

    m1 = ArrayDifference(arr1,arr2)

    print(m1.difference())

