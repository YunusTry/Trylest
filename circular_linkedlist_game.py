class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("Circular linked list is empty")
            return
        itr = self.head
        llstr = ''
        while True:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
            if itr == self.head:
                break
        print(llstr)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head.next = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        itr = self.head
        while itr.next != self.head:
            itr = itr.next
        itr.next = new_node
        new_node.next = self.head

    def insert_at(self, index, data):
        if index < 0:
            raise Exception("Invalid Index")

        new_node = Node(data)
        if index == 0:
            if self.head is None:
                new_node.next = new_node
                self.head = new_node
            else:
                itr = self.head
                while itr.next != self.head:
                    itr = itr.next
                itr.next = new_node
                new_node.next = self.head
                self.head = new_node
        else:
            count = 0
            itr = self.head
            while count < index - 1:
                itr = itr.next
                count += 1
            new_node.next = itr.next
            itr.next = new_node

    def remove_at(self, index):
        if index < 0:
            raise Exception("Invalid Index")

        if index == 0:
            if self.head is None:
                return
            if self.head.next == self.head:
                self.head = None
            else:
                itr = self.head
                while itr.next != self.head:
                    itr = itr.next
                self.head = self.head.next
                itr.next = self.head
        else:
            count = 0
            itr = self.head
            while count < index - 1:
                itr = itr.next
                count += 1
            itr.next = itr.next.next

class CircularLinkedListGame:
    def __init__(self):
        self.cll = CircularLinkedList()

    def play_game(self):
        current_node = self.cll.head
        step_size = current_node.data
        while current_node.next != current_node:
            for _ in range(step_size - 1):
                current_node = current_node.next
            removed_data = current_node.next.data
            current_node.next = current_node.next.next
            step_size = removed_data
            print(f"Removed: {removed_data}")
            cll_game.cll.print()
            
        return current_node.data

if __name__ == '__main__':
    cll_game = CircularLinkedListGame()
    cll_game.cll.insert_at_beginning(1)
    cll_game.cll.insert_at_end(1)
    cll_game.cll.insert_at(1, 2)
  

    cll_game.cll.print()

    winner = cll_game.play_game()
    print("Kazanan:", winner)

