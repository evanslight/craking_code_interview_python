# quicksort time complexity is O(NlogN) space complexity is O(logN) the space complexity is for the bound index. The most important procedure random can gurantee the O(NlogN) to some extends.
# www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html
import random
class QuickSort():
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def partition(self, arr, L, R):
        num = arr[R]
        less = L - 1
        more = R 
        cur = L
        while (cur < more):
            if(arr[cur] < num):
                less += 1
                self.swap(arr, cur, less)
                cur += 1
            elif(arr[cur] == num):
                cur += 1
            else:
                more -= 1
                self.swap(arr, cur, more)
        print(arr[more], arr[R])
        self.swap(arr, more, R)
        return [less + 1, more]

    def quicksort(self, arr, L, R):
        if(L < R):
            # random to insure the NlogN
            self.swap(arr, random.randint(L, R), R)
            bound = self.partition(arr, L, R)
            self.quicksort(arr, L, bound[0] - 1)
            self.quicksort(arr, bound[1] + 1, R)
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
    mySort = QuickSort()
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    print("unsorted array is ", arr)

    print(mySort.getMax(arr, 0, len(arr) - 1))

    arrSorted = mySort.quicksort(arr, 0, len(arr) - 1)
    print("my sorted array is ", arrSorted)

    if(rightAnswer(arr) == arrSorted):
        print("true")
    else:
        print("the answer is incorrect.")

