                node = node.next

            item = node.next.data # extract the data
            node.next = None      # detach the last node
            return item           # return the data


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