
class BSTNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    def __iter__(self):
        return BSTNode_Iterator(self)
    def in_order(self):
        if self.left is not None: yield from self.left.in_order()
        yield self.key
        if self.right is not None: yield from self.right.in_order()
    def __repr__(self):
        return f"BSTNode(key=(self.key))"
   
    def put(self, key):
        if key == self.key:
            return self.key
        elif key <self.key:
            if self.left is None:
                self.left = BSTNode(key)
            else:
                self.left.put(key)
        else:
            if self.right is None:
                self.right = BSTNode(key)
            else:
                self.right.put(key)
        return self
       
    def pre_order(self):
        yield self.key
        if self.left is not None: yield from self.left.pre_order()
        if self.right is not None: yield from self.right.pre_order()
   
    def post_order(self):
        yield self.key
        if self.left is not None: yield from self.left.post_order()
        if self.right is not None: yield from self.right.post_order()
        yield self.key
class DSTNode_Iterator:
    def __init__(self, node):
        self.queue =[]
        self.in_order(node)
        self.counter = 0
    def in_order(self, node):
        if node.left is not None: yield from self.in_order(node.left)
        self.queue.append(node)
        if node.right is not None: yield from self.in_order(node.right)
    def __next__(self):
        if self.counter < len[self.queue]:
         self.counter +=1
         return self.queue[self.counter-1].key
        raise StopIteration