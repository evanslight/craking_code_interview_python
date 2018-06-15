# use two queue to form a stack 
import random
from collections import deque
class queue_stack():
    __queue1 = deque()
    __queue2 = deque()

    def push(self, item):
        self.__queue1.append(item)

    def pop(self):
        if (self.__queue1 == []):
            print("the stack is empty")
            return
        while (len(self.__queue1) > 1):
            self.__queue2.append(self.__queue1.popleft())

        self.swap()
        return self.__queue2.popleft()

    def swap(self):
        tmp = []
        tmp = self.__queue1
        self.__queue1 = self.__queue2
        self.__queue2 = tmp


if __name__ == "__main__":
    size = 3
    myStack = queue_stack()
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    print("the arr is ", arr)
    for i in range(0, size):
        myStack.push(arr[i])

    for i in range(0, size):
        print(myStack.pop())


