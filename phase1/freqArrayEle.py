class Frequency:
    def __init__(self, arr, item):
        self.arr = arr
        self.item = item

    def get_frequency(self):
        count = 0

        if item not in arr:
            return count
        else:
            for i in self.arr:
                if i == self.item:
                    count += 1

        return count

if __name__ == "__main__":
    arr = [x for x in input("Enter array elements space seperated").split()]
    item = input("Enter the item whose frequency you want to know")

    f1 = Frequency(arr, item)
    print(f1.get_frequency())
