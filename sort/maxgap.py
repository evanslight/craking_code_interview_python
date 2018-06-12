# given an array, after sorted, what is the max difference between two adjacent numbers. the time 
# complexity should be O(N) and only sort based on comparison is permitted.
import random
import sys
import array
class MaxGap():
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    def maxGap(self, nums):
        if(nums is None or len(nums) < 2):
            return 0
        length = len(nums)
        # in python3 there is no maxint. only maxsize
        minv = sys.maxsize
        maxv = -sys.maxsize - 1

        for _ in range(0, length):
            minv = min(nums[_], minv)
            maxv = max(nums[_], maxv)

        if (minv == maxv):
            return 0
        maxs = [-sys.maxsize-1] * (length+1)
        mins = [sys.maxsize] * (length+1)
        hasNum = [0] * (length+1)
        bid = 0
        for _ in range(0, length):
            bid = self.bucket(nums[_], length, minv, maxv)
            mins[bid] = nums[_] if hasNum[bid] else min(nums[_], mins[bid])
            maxs[bid] = nums[_] if hasNum[bid] else max(nums[_], maxs[bid])
            hasNum[bid] = 1
        print(mins)
        res = 0
        lastMax = maxs[0]
        for i in range(1, length+1):
            if(hasNum[i]):
                temp = mins[i] - lastMax
                res = max(res, temp)
                lastMax = maxs[i]
        return res

    def bucket(self, num, length, minv, maxv):
        return int((num - minv) * length / (maxv - minv))

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
    mySort = MaxGap()
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    print("unsorted array is ", arr)

    print(mySort.getMax(arr, 0, len(arr) - 1))

    arrSorted = mySort.maxGap(arr)
    print("my sorted array is ", arrSorted)

    if(rightAnswer(arr) == arrSorted):
        print("true")
    else:
        print("the answer is incorrect.")

