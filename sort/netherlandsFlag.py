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
class NetherlandsFlag():
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def partition(self, arr, L, R, num):
        less = L - 1
        more = R + 1
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
    mySort = NetherlandsFlag()
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    num = 15
    arr.append(num)
    arr.append(num)
    print("unsorted array is ", arr)

    print(mySort.getMax(arr, 0, len(arr) - 1))

    arrSorted = mySort.partition(arr, 0, len(arr) - 1, num)
    print("my sorted array is ", arrSorted)

    if(rightAnswer(arr) == arrSorted):
        print("true")
    else:
        print("the answer is incorrect.")

