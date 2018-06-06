# merge sort, it starts with the i=1 position, each time j would check wheter there is a number existed which is smaller than that. if it does than change it 
# in worst case, the complexity is O(n^2), the reason is it sums n+n-1+n-2+...+1, it's a arithmetic progression
# master theorem is T(N) = a*T(N/b) + O(N^d)
# a represents how many times that the seperation occur
# N/b represents the size of the child sample
# n^d stands for the complexity of the remained procedures(such as comparison)
# log(b,a) > d -> O(N^log(b,a))
# log(b,a) = d -> O(N^d * logN)
# log(b,a) < d -> O(N^d)
# www.gocalf.com/blog/algorithm-complexity-and-master-theorem.html
import random
class MergeSort():
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def mergeSort(self, arr):
        if(arr is None or len(arr) < 2): 
            return
        self.sortProcess(arr, 0, len(arr) - 1)
        return arr

    def sortProcess(self, arr, left, right):
        if (left == right):
            return

        # here int conversion is a must, otherwise mid would be float
        mid = int(left + (right - left) / 2)
        self.sortProcess(arr, left, mid)
        self.sortProcess(arr, mid + 1, right)
        self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        tempList = []
        p1 = left
        p2 = mid + 1

        while (p1 <= mid and p2 <= right):
            if(arr[p1] >= arr[p2]):
                tempList.append(arr[p2])
                p2 += 1
            else:
                tempList.append(arr[p1])
                p1 += 1

        while(p1 <= mid):
            tempList.append(arr[p1])
            p1 += 1
        while(p2 <= right):
            tempList.append(arr[p2])
            p2 += 1

        # here len(tempList) cannot be len(tempList) - 1, since range would ignore len(tempList) - 1
        for x in range(0, len(tempList)):   
            arr[left + x] = tempList[x]

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
    mySort = MergeSort()
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    print("unsorted array is ", arr)

    print(mySort.getMax(arr, 0, len(arr) - 1))

    arrSorted = mySort.mergeSort(arr)
    print("my sorted array is ", arrSorted)

    if(rightAnswer(arr) == arrSorted):
        print("true")
    else:
        print("the answer is incorrect.")

