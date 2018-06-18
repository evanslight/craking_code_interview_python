# given a matrix with integers. please print it in the spiral order way
# the space complexity should be O(1)
import numpy as np
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 1

    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


class IsPalindrome:
    
    # use stack to save the tranversed linkedlist and check back. the space copmplexity is o(N)
    def check(self, linkedlist):
        temp = linkedlist.head
        check_stack = []
        length = 1
        while (temp):
            check_stack.append(temp.data)
            length += 1
            temp = temp.next

        temp = linkedlist.head
        index = 0
        while (temp):
            if(check_stack.pop() != temp.data):
                print("it's not palindrome!")
                return
            index += 1
            temp = temp.next
        
        if(index == length - 1):
            print("this is palindrome.")
   
    # use head.next.next to stop the tranverse. the space complexity is O(N)
    def check_jump(self, linkedlist):
        temp = linkedlist.head
        if (temp is None or temp.next is None):
            print("this is palindrome")
            return
        check_stack = []
        quick = temp
        check_stack.append(temp.data)
        while (quick.next and quick.next.next):
            check_stack.append(temp.next.data)
            temp = temp.next
            quick = quick.next.next
        print(check_stack) 

        if (quick.next is not None):
            temp = temp.next

        while (temp):
            if (check_stack.pop() != temp.data):
                print("not palindrome.")
                return
            temp = temp.next

        if(temp is None):
            print("this is palindrome")

    # check the linkedlist with the inverse 
    def check_inverse(self, linkedlist):
        temp = linkedlist.head
        if (temp is None or temp.next is None):
            print("this is palindrome")
            return
        # locate the middle of linkedlist and reverse the right part
        quick = temp
        while (quick.next and quick.next.next):
            temp = temp.next
            quick = quick.next.next
        n1 = temp
        n2 = n1.next
        n1.next = None
        while (n2 is not None):
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3

        # check the palindrome
        n3 = n1
        n2 = linkedlist.head
        res = True
        while (n1 is not None and n2 is not None):
            if (n2.data != n2.data):
                print("not palindrome")
                res = False
                return
            n2 = n2.next
            n1 = n1.next
        if (res == True):
            print("this is palindrome")
        
        # reverse the linkedlist back
        n1 = n3.next
        n3.next = None
        while(n1 is not None):
            n2 = n1.next
            n1.next = n3
            n3 = n1
            n1 = n2
        return




if __name__ == "__main__":
    list_temp = LinkedList()
    list_temp.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth  = Node(2)
    fifth  = Node(1)
    #sixth  = Node(1)

    list_temp.head.next = second
    second.next = third
    third.next = fourth 
    fourth.next = fifth
    #fifth.next = sixth

    list_temp.print_list()

    check_palindrome = IsPalindrome()
    check_palindrome.check(list_temp)
    check_palindrome.check_jump(list_temp)
    check_palindrome.check_inverse(list_temp)
