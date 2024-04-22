class Entry:
 def __init__(self, item, priority):
  self.item = item
  self.priority = priority

 def lt(self, other):
  return self.priority < other.priority

 def eq(self, other):
   return self.priority == other.priority and self.item == other.item

class PQ_UL:
 def __init__(self):
  self.list=[]
 def __len__(self):
  return len(self.list)
 def insert(self, item, priority):
  self.list.append(Entry(item, priority))
 def find_min(self):
  return self.list.min()
 def remove_min(self):
  return self.list.pop(0)

class PQ_OL:
 def __init__(self):
  self.list[]
 def insert(self, item, priority):
  self.list.append(Entry(item,priority))
  self.list.sort(reverse = True)
 def find_min(self)
   return self.list[-1]
 def remove_min (self):
  return self.list.pop(-1)
