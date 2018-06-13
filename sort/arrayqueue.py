# quicksort time complexity is O(NlogN) space complexity is O(logN) the space complexity is for the bound index. The most important procedure random can gurantee the O(NlogN) to some extends.
# www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html
import random
class arrayQueue():
    __size = 0
    __start = 0
    __end = 0
    __arr = []

    def __init__(self, initsize):
        if (size < 0):
            return
        self.__arr = [0] * initsize
        self.__size = 0
        self.__start = 0
        self.__end == 0

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def peek():
        if (self.__size == 0):
            return
        return self.__arr[self.__start]

    def push(self, obj):
        if (self.__size == len(self.__arr)):
            print("array index out of bounds")
            return
        self.__size += 1
        self.__arr[self.__end] = obj
        self.__end = 0 if len(self.__arr) -1 == self.__end else self.__end + 1

    def poll(self):
        if (self.__size == 0):
            print("array index out of bounds")
        self.__size -= 1
        temp = self.__start
        self.__start = 0 if len(self.__arr) -1 == self.__start else self.__start + 1
        return self.__arr[temp]

    

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
    myStack = arrayQueue(size)
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    print("the arr is ", arr)
    for i in range(0, size):
        myStack.push(arr[i])

    for i in range(0, size):
        print(myStack.poll())


