# for bubbleSort find the biggest number and put it at the "last" postiona
# the complexity is O(n^2), the reason is it sum n+n-1+n-2+...+1, it's a 
# arithmetic progression
class BubbleSort():
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def bubbleSort(self, arr):
        if(arr is None or len(arr) < 2): 
            return
        for i in range(len(arr)-1,0,-1):
            for j in range(0,i):
                print("aaa")
                if(arr[j] > arr[j+1]):
                    self.swap(arr,i,j)
        return arr

if __name__ == "__main__":
    bubblesort = BubbleSort()
    arr=[5,4,3,2,1]
    print(bubblesort.bubbleSort([5,4,3,2,1]))

