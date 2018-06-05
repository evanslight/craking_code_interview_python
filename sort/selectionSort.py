# for selection sort, it finds the smallest number and put it at the "first"position 
# the complexity is O(n^2), the reason is it sumn+n-1+n-2+...+1, it's a 
# arithmetic progression
class SelectionSort():
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def selectionSort(self, arr):
        if(arr is None or len(arr) < 2): 
            return
        cnt = 0
        for i in range(0,len(arr)):
            for j in range(i+1,len(arr)):
                print(cnt)
                cnt += 1
                if(arr[i] > arr[j]):
                    self.swap(arr,i,j)
        return arr

if __name__ == "__main__":
    sort = SelectionSort()
    arr=[5,4,3,2,1]
    print(sort.selectionSort([5,4,3,2,1]))

