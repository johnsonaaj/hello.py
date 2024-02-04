
def generic_hi (name): 
  greeting = "Hello, " + name + "!"
  if len(name) == 0 :
   name = "world!"
  return greeting  

me = generic_hi(name) 
print(me) 
 