# heapsort the most important one, which achieve the logN when do insertions.
# heapsort: time complexity is NlogN space complexity is O(1)
# heapbuilding(heapInsert): time complexity is O(N)
# www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html
import random
class HeapSort():
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def heapInsert(self, arr, index):
        parent = int((index - 1) / 2)
        while(arr[index] > arr[parent]):
            self.swap(arr, index, parent)
            index = parent
            parent = int((index - 1) / 2)

    def heapify(self, arr, index, size):
        left = 2 * index + 1
        while (left < size):
            if(left + 1 < size and arr[left] < arr[left + 1]):
                largest = left + 1
            elif(left + 1 < size and arr[left] >= arr[left + 1]):
                largest = left
            else:
                largest = left
            if(arr[index] < arr[largest]):
                largest = largest
            else:
                largest = index
            if(arr[index] == arr[largest]):
                break
            
            self.swap(arr, index, largest)
            index = largest
            left = 2 * index + 1

    def heapsort(self, arr):
        if(arr is None or len(arr) < 2):
            return
        # insert one by one from array and form the big root heap
        for i in range(0, len(arr)):
            self.heapInsert(arr, i)
        
        # put the largest number to the last position and heapsize-- to keep it always there
        size = len(arr) - 1
        self.swap(arr, 0, size)
        while(size > 0):
            self.heapify(arr, 0, size)
            size -= 1
            self.swap(arr, 0, size)

        return arr

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
    mySort = HeapSort()
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    print("unsorted array is ", arr)

    print(mySort.getMax(arr, 0, len(arr) - 1))

    arrSorted = mySort.heapsort(arr)
    print("my sorted array is ", arrSorted)

    if(rightAnswer(arr) == arrSorted):
        print("true")
    else:
        print("the answer is incorrect.")

