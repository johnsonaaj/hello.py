



def solve_puzzle(title_L):
      m_list = []
      return solve_puzzle1(title_L, 0, m_list)
def solve_puzzle1(title_L, index_v, m_list):
      if index_v == len(title_L) -1:
           return True
      elif index_v in m_list:
           return False
      m_list.append(index_v)
      clock_index =(index_v + title_L[index_v]) % len(title_L)
      count_index =(index_v - title_L[index_v]) % len(title_L)
      if solve_puzzle1(title_L, clock_index, m_list):
       return True
      m_list.remove(index_v)
      return False
