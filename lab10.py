class Entry:
 def __init__(self, item, priority):
  self.item = item
  self.priority = priority

 def lt(self, other):
  return self.priority < other.priority

 def eq(self, other):
   return self.priority == other.priority and   self.item == other.item
class PriorityQueue(List):
 def __len__(self):
  return len(self)

 def insert(self, item, priority):
  self.append(Entry(item, priority))

 def find_min(self):
  return self.min()

 def remove_min(self):
  return self.pop(0)

