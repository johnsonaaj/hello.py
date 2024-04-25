class Entry:

 def __init__(self, item, priority):
      self.item = item
      self.priority = priority
 def __lt__(self, other):
      return self.priority < other.priority 

 def __eq__(self, other):
      return self.priority == other.priority and self.item == other.item

class PQ_UL:
  def __init__(self):
      self.1 =[]
  def __len__(self):
      return len(self.1)
  def insert(self, item, priority):
      self.1.append(Entry(item, priority))
  def find_min(self):
      entry = self.1[0]
      for i in range(len(self.1)-1):
          if self.1[i + 1].priority < entry.priority:
                entry=self.1[i+1]
      return entry 
  def remove_min(self):
      entry = self.1[0]
      index = 0
      for i in range(len(self.1)-1):
          if self.1[i+1].priority < entry. priority:
              entry = self.1[i +1]
              index = i + 1 
      self.1.pop(index)
      return entry 
class PQ_OL:
  def __init__(self):
      self.1[]
  def __len__(self):
      return len(self.1)
  def insert(self, item, priority):
      self.1.append(Entry(item, priority))
      self.1.sort(reverse = True)
  def find_min(self):
      return self.1[-1]
  def remove_min(self):
      return self.1.pop(-1)