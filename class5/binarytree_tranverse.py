# implement binary tree pre order, in order and post order, including recursive and non-recursive way
class Node:
    def __init__(self, data):
        self.data = data
        left = None
        right = None

class BinaryTreeTran:
    def pre_order_recu(self, head):
        if (head is None):
            return
        print(head.data, end=" ")
        self.pre_order_recu(head.left)
        self.pre_order_recu(head.right)

    def in_order_recu(self, head):
        if (head is None):
            return
        self.in_order_recu(head.left)
        print(head.data, end=" ")
        self.in_order_recu(head.right)

    def pos_order_recu(self, head):
        if (head is None):
            return
        self.pos_order_recu(head.left)
        self.pos_order_recu(head.right)
        print(head.data, end=" ")

    def pre_order_iter(self, head):
        if (head is not None):
            stack = []
            stack.append(head)
            while (len(stack) > 0):
                head = stack.pop()
                print(head.data, end=" ")
                if (head.right is not None):
                    stack.append(head.right)
                if (head.left is not None):
                    stack.append(head.left)

    def in_order_iter(self, head):
        if (head is not None):
            stack = []
            while (len(stack) > 0 or head is not None):
                if (head is not None):
                    stack.append(head)
                    head = head.left
                else:
                    head = stack.pop()
                    print(head.data, end=" ")
                    head = head.right

    def pos_order_iter(self, head):
        if (head is not None):
            print_stack = []
            stack = []
            stack.append(head)
            while (len(stack) > 0):
                head = stack.pop()
                print_stack.append(head)
                if (head.left is not None):
                    stack.append(head.left)
                if (head.right is not None):
                    stack.append(head.right)
            
            while (len(print_stack) > 0):
                print(print_stack.pop().data, end=" ")

if __name__=="__main__":
    print("hello")
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.left = None
    root.left.left.right = None
    root.left.right.left = None
    root.left.right.right = None
    root.right.left.left = None
    root.right.left.right = None
    root.right.right.left = None
    root.right.right.right = None

    # begin tranverse
    tranverse = BinaryTreeTran()
    tranverse.pre_order_recu(root)
    print()
    print("===")
    tranverse.in_order_recu(root)
    print()
    print("===")
    tranverse.pos_order_recu(root)
    print()
    print("===")
    tranverse.pre_order_iter(root)
    print()
    print("===")
    tranverse.in_order_iter(root)
    print()
    print("===")
    tranverse.pos_order_iter(root)
