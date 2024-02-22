class LinkedList:
    def __init__(self):
        self._head = None

    def add_first(self, data):
        self._head = Node(data, next=self._head)

    def remove_first(self):
        if self._head is None:
            raise Exception("Linked list is empty")
        data = self._head.data
        self._head = self._head.next
        return data

    def add_last(self, data):
        if self._head is None:
            self._head = Node(data)
        else:
            current = self._head
            while current.next:
                current = current.next
            current.next = Node(data)

    def remove_last(self):
        if self._head is None:
            raise Exception("Linked list is empty")
        elif self._head.next is None:
            data = self._head.data
            self._head = None
            return data
        else:
            current = self._head
            while current.next.next:
                current = current.next
            data = current.next.data
            current.next = None
            return data


if __name__ == '__main__':
    ##########Test Node##########
    n1 = Node(1)
    assert(n1.data==1)
    n2 = Node(2, next=n1)
    assert(n2.data == 2)
    assert(n2.next == n1)

    ##########Test LinkedList##########
    ll1 = LinkedList()
    assert(ll1._head == None)

    #add_first()
    for i in range(10):
        ll1.add_first(i*3)
        assert(ll1._head.data == i*3)

    #remove_first()
    for i in range(9,-1,-1):
        assert(ll1.remove_first() == i*3)

    #add_last()
    ll1 = LinkedList()
    for i in range(10):
        ll1.add_last(i*2)

    for i in range(10):
        assert(ll1.remove_first() == i*2)

    #remove_last()
    ll1 = LinkedList()
    for i in range(10):
        ll1.add_first(i*7)

    for i in range(10):
        assert(ll1.remove_last() == i*7)