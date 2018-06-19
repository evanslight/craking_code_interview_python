# netherlands problem in linkedlist but the space complexity is O(1)
import numpy as np
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


class NetherlandsLinklist:
    def partition_linkedlist(self, head, pivot):
        sH = None
        sT = None
        eH = None
        eT = None
        bH = None
        bT = None
        next = None

        while (head != None):
            next = head.next
            head.next = None
            if (head.data < pivot):
                if (sH is None):
                    sH = head
                    sT = head
                else:
                    sT.next = head
                    sT = head
            elif (head.data == pivot):
                if (eH is None):
                    eH = head
                    eT = head
                else:
                    eT.next = head
                    eT = head
            else:
                if (bH is None):
                    bH = head
                    bT = head
                else:
                    bT.next = head
                    bT = head
            head = next

        if (sT is not None):
            sT.next = eH
            eT = sT if eT is None else eT

        if (eT is not None):
            eT.next = bH

        return sH if sH is not None else eH if eH is not None else bH




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

    partition = NetherlandsLinklist()

    newhead = partition.partition_linkedlist(list_temp.head, 2)
    list_temp.head = newhead
    list_temp.print_list()
