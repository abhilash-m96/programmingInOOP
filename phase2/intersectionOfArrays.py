class ArrayIntersection:
    def __init__(self, arr1, arr2):
        self.arr1 = arr1
        self.arr2 = arr2

    def intersection(self):
        res = []

        for item in self.arr1:
            if item in self.arr2:
                res.append(item)

        return res

if __name__ == "__main__":
    arr1 = [ x for x in input("Enter items of first array seperated by space \n").split() ]
    arr2 = [ x for x in input("Enter items of second array seperated by space \n").split() ]

    m1 = ArrayIntersection(arr1,arr2)

    print(m1.intersection())

