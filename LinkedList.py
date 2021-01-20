class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class linkedList:
    def __init__(self):
        self.head = None

    def insert_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty!")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr = llstr + str(itr.data) + '-->'
            itr = itr.next
        
        print(llstr)


if __name__ == '__main__':
    ll = linkedList()
    ll.insert_beg(10)
    ll.insert_beg(5)
    ll.print()