class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node

    def append(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next

            last.next = Node(data, None, last)

    def printf(self):
        if self.head is None:
            print("Linked List is Empty!")
            return
        itr = self.head
        dllstr = 'Null -> '
        while itr:
            dllstr = dllstr + str(itr.data) + ' -> '
            itr = itr.next

        dllstr += 'Null'

        print(dllstr)

    def printb(self):
        if self.head is None:
            print("Linked List is Empty!")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        dllstr = 'Null -> '
        while itr:
            dllstr = dllstr + str(itr.data) + ' -> '
            itr = itr.prev

        dllstr += 'Null'
        print(dllstr)

    def pop(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None

    def remove(self, value):
        itr = self.head
        while itr:
            if itr.data == value:
                itr.prev.next, itr.next.prev = itr.next, itr.prev
            itr = itr.next


if __name__ == '__main__':
    dll = DoublyLinkedList()
    dll.prepend(4)
    dll.prepend(3)
    dll.prepend(2)
    dll.prepend(1)

    dll.append(5)
    dll.append(6)
    dll.append(7)

    dll.printf()
    dll.pop()
    dll.printb()
    dll.remove(5)
    dll.printf()
