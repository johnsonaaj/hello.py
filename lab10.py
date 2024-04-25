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
      self.l =[]
  def __len__(self):
      return len(self.l)
  def insert(self, item, priority):
      self.l.append(Entry(item, priority))
  def find_min(self):
      entry = self.l[0]
      for i in range(len(self.l)-1):
          if self.l[i + 1].priority < entry.priority:
                entry=self.l[i+1]
      return entry 
  def remove_min(self):
      entry = self.l[0]
      index = 0
      for i in range(len(self.l)-1):
          if self.l[i+1].priority < entry. priority:
              entry = self.l[i +1]
              index = i + 1 
      self.l.pop(index)
      return entry 
class PQ_OL:
  def __init__(self):
      self.l=[]
  def __len__(self):
      return len(self.l)
  def insert(self, item, priority):
      self.l.append(Entry(item, priority))
      self.l.sort(reverse = True)
  def find_min(self):
      return self.l[-1]
  def remove_min(self):
      return self.l.pop(-1)