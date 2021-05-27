class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty!")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr = llstr + str(itr.data) + ' -> '
            itr = itr.next
        llstr += 'NULL'
        print(llstr)

    def add(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, dataList):
        self.head = None
        for data in dataList:
            self.add(data)

    def length(self):
        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove(self, value):
        itr = self.head
        count = 0
        while itr:
            if itr.data == value:
                self.remove_at(count)
                break

            itr = itr.next
            count += 1
        else:
            print('Value Not Found!')

    def insert_after(self, data, value):
        itr = self.head
        while itr:
            if itr.data == value:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next


if __name__ == '__main__':
    ll = linkedList()
    ll.insert(10)
    ll.insert(5)
    ll.add(15)
    ll.print()
    print('Length:', ll.length())
    ll.insert_values([323, 23432, 423, 4, 324, 23, 44])
    ll.print()
    print('Length:', ll.length())
    print()
    ll.remove_at(1)
    ll.print()
    print()
    ll.insert_at(0, 1)
    ll.print()
    ll.insert_at(3, 222)
    ll.print()

    ll.remove(23)
    ll.print()

    print()

    ll.insert_after(100, 4)
    ll.print()
