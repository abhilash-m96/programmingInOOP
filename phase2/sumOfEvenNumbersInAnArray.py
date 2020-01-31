class SumOfEvenNumbers:
    def __init__(self, arr):
        self.arr = arr

    def even_sum(self):
        sum = 0

        for num in self.arr:
            if num % 2 == 0:
                sum += num

        return sum

if __name__ == "__main__":
    arr = [int(x) for x in input("Enter the numbers of the array space seperated \n").split()]
    s1 = SumOfEvenNumbers(arr)

    print(s1.even_sum())

