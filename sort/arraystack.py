# quicksort time complexity is O(NlogN) space complexity is O(logN) the space complexity is for the bound index. The most important procedure random can gurantee the O(NlogN) to some extends.
# www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html
import random
class stackArray():
    __index = 0
    __arr = []

    def __init__(self, size):
        if (size < 0):
            return
        self.__arr = [0] * size
        self.__index = 0

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def push(self, obj):
        if (self.__index == len(self.__arr)):
            print("array index out of bounds")
            return

        self.__arr[self.__index] = obj
        self.__index += 1
        print(self.__arr)

    def pop(self):
        if (self.__index == 0):
            print("array index out of bounds")
        self.__index -= 1
        return self.__arr[self.__index]

    

    # get the maximum value
    def getMax(self, arr, left, right):
        if(left == right):
            return arr[left]
        # int conversion is a must, otherwise mid would get float number
        mid = int(left + (right - left) / 2)
        maxleft = self.getMax(arr, left, mid)
        maxright = self.getMax(arr, mid + 1, right)
        return max(maxleft, maxright)

def rightAnswer(arr):
    return sorted(arr)

if __name__ == "__main__":
    size = 3
    myStack = stackArray(size)
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    print("the arr is ", arr)
    for i in range(0, size):
        myStack.push(arr[i])

    for i in range(0, size):
        print(myStack.pop())


