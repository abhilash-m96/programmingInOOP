# Find the first and the second biggest elements in a user given array

class FirstAndSecondBiggest:
    def __init__(self, arr):
        self.arr = arr

    def find(self):
        if len(self.arr) == 0:
            return None
        else:
            first_big = arr[0]
            sec_big = arr[1]

            for i in range(len(arr)):
                if arr[i] > first_big:
                    first_big = arr[i]
                elif arr[i] < first_big and arr[i] > sec_big:
                    sec_big = arr[i]

            return first_big, sec_big

if __name__ == "__main__":
    arr = [x for x in input("Enter the array elements space seperated \n").split() ]
    f1 = FirstAndSecondBiggest(arr)
    print(f1.find())

