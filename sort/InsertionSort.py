# for insertion sort, it starts with the i=1 position, each time j would check wheter there is a number existed which is smaller than that. if it does than change it 
# in worst case, the complexity is O(n^2), the reason is it sums n+n-1+n-2+...+1, it's a arithmetic progression
# in best case. the complexity is O(n)
import random
class InsertionSort():
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def insertionSort(self, arr):
        if(arr is None or len(arr) < 2): 
            return
        cnt = 0
        for i in range(1, len(arr)):
            for j in range(i-1,-1,-1):
                cnt += 1
                if(arr[j] > arr[j+1]):
                    self.swap(arr,j,j+1)
                else:
                    break
        print("number of loops is ", cnt)

        return arr

def rightAnswer(arr):
    return sorted(arr)

if __name__ == "__main__":
    mySort = InsertionSort()
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    print("unsorted array is ", arr)
    arrSorted = mySort.insertionSort(arr)
    print("my sorted array is ", arrSorted)
    if(rightAnswer(arr) == arrSorted):
        print("true")

