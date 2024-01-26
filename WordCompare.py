def word_compare(str1, str2): 
 if not isinstance(str1, str) or not
sinstance(str2, str): 
  return ""Those aren't strings" 

if sorted(str1) == sorted(str2): 
  return "Anagram" 
  return (str1, str2)
