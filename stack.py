class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data, self.head)
        self.head = node

    def pop(self):
        if self.head:
            self.head = self.head.next
        else:
            print("stack is empty")

    def print(self):
        itr = self.head
        while itr:
            print("|")
            print(itr.data)
            itr = itr.next
        print("---------------------")

ll = Stack()  

ll.add(4)
ll.print()
ll.add(2)
ll.print()
ll.add(3)
ll.print()
ll.pop()
ll.print()
ll.pop()
ll.print()
ll.pop()
ll.print()
ll.pop()
ll.print()

        
