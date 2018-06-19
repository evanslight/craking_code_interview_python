# copy a linkedlist with random pointers
import numpy as np
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.rand = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            if(temp is not None and temp.rand is not None):
                print("random number is ", temp.rand.data)

            temp = temp.next


class CopyLinklist:
    def copy_hash(self, head):
        cur = head
        map = {}
        while (cur is not None):
            map[cur] = Node(cur.data)
            cur = cur.next
        print(map)
        cur = head
        while (cur is not None):
            if (cur.next is not None):
                map[cur].next = map[cur.next]
            else:
                map[cur].next = None

            if (cur.rand is not None):
                map[cur].rand = map[cur.rand]
            else:
                map[cur].rand = None

            cur = cur.next
        return map[head]

    def copy_origin(self, head):
        if (head is None):
            return None
        cur = head
        next = None

        # copy node and link to every node
        while (cur is not None):
            next = cur.next
            cur.next = Node(cur.data)
            cur.next.next = next
            cur = next

        # set copy node rand
        cur = head
        cur_copy = None
        while (cur is not None):
            next = cur.next.next
            cur_copy = cur.next 
            cur_copy.rand = cur.rand.next if cur.rand is not None else None
            cur = next

        # split
        res = head.next
        cur = head
        while (cur != None):
            next = cur.next.next
            cur_copy = cur.next
            cur.next = next
            cur_copy.next = next.next if next is not None else None
            cur = next
        return res

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

    list_temp.head.rand = list_temp.head.next.next
    list_temp.head.next.rand = list_temp.head.next.next.next.next

    list_temp.print_list()

    copyed_list = CopyLinklist()
    list_temp.head = copyed_list.copy_hash(list_temp.head)
    list_temp.print_list()
    list_temp.head = copyed_list.copy_origin(list_temp.head)
    list_temp.print_list()


