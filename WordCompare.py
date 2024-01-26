
def word_compare(stri=None, str2=None): 
 if str1 is None or str2 is None: 
  return "Those aren't strings" 
 if not isinstance(str1, str) or not isinstance(str2, str): 
  return "Those aren't strings" 
 if sorted(str1) == sorted(str2): 
  return "Anagram return (str1, str2)