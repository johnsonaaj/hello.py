class Entry:
 def __init__(self, item, priority):
  self.item = item
  self.priority = priority

 def lt(self, other):
  return self.priority < other.priority

  PQ.UL = PriorityQueue(unordered_list)
  PQ.OL = PriorityQueue(ordered_list)

class PriorityQueue(List):
 def __len__(self):
  return len(self)

 def insert(self, item, priority):
  self.append(Entry(item, priority))

 def find_min(self):
  return self.min()

 def remove_min(self):
  return self.pop(0)

