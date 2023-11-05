class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None

    def add(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def pop(self):
        if self.head:
            self.head = self.head.next
        else:
            print("stack is empty")
    def print(self):
        itr = self.head
        llstr =''
        while itr:
            llstr += str(itr.data) + ' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

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
