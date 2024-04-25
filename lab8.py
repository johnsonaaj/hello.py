class CustomSet:
  def __init__(self):
    self._min_buckets = 8 
    self._n_buckets = 8
    self._len = 0 
    self._L = [[] for i in range(self._n_buckets)]
  def __len__(self):
    return self._len
  def _find_bucket(self, item):
    hash = hash(item) 
    return (hash % self._n_buckets) 
  def __contains__(self, item):
    if item in self._L[val]:
      return True
    else:
      return False 
  def add(self, item):
    if item in self:
      return
    else:
      idx = self._find_bucket(item) 
      self._L[idx].append(item)
      self._len += 1
      if self.len >= 2*(self._n_buckets):
        self._rehash(2*self._n_buckets)
  def remove (self, item):
     if item not in self:
       raise KeyError("the item is not in set")
     idx = self._find_bucket(item)
     if item in self._L[idx]:
       self._len -= 1
       if self._len <= ((1/2)*self._n_buckets) and self._min_buckets <= ((1/2)*self._n_buckets):
           self._rehash(self._n_buckets // 2)
  def _rehash(self, new_buckets):
      self._n_buckets = new_buckets
      new_L = [[] for i in range(new_buckets)] 
      for bucket in self._L:
        for item in bucket: 
            new_idx = hash(item) % new_buckets
            new_L[new_idx].append(item) 

