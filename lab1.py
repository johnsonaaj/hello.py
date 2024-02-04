
def generic_hi (name): 
  greeting = "Hello, " + name + "!"
  if len(name) == 0 :
   name = "world!"
  return greeting  

print(generic_hi())