
from BSTNode import BTSNode

class BSTSet:
    def __init__(self):
        self._head = None
    def __iter__(self):
        return iter[self._head]
    def in_order(self):
        if self._head is not None:
            yield from self._head._in_order()
           
    def put(self,key):
        if self._head is None:
            self._head =BSTNode(key)
        else:
            self._head.put(key)
           
    def pre_order(self):
        if self._head is not None:
            yield from self._head.pre_order()
    def post_order(self):
        if self._head is not None:
            yield from self._head.post_order()