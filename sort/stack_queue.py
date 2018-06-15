# use two stack to form a queue
import random
class stack_queue():
    __stackPush = []
    __stackPop = []

    def push(self, item):
        self.__stackPush.append(item)
        self.transfer()

    def poll(self):
        if (self.__stackPush == [] and self.__stackPop == []):
            print("the queue is empty")
            return
        self.transfer()
        return self.__stackPop.pop()

    def transfer(self):
        if (self.__stackPop != []):
            return
        while (self.__stackPush != []):
            self.__stackPop.append(self.__stackPush.pop())


if __name__ == "__main__":
    size = 3
    myStack = stack_queue()
    arr = [ random.randint(0,30) for x in range(random.randint(5,10)) ]
    print("the arr is ", arr)
    for i in range(0, size):
        myStack.push(arr[i])

    for i in range(0, size):
        print(myStack.poll())


