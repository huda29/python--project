# Python Loops 3 
# For Loop 
#The range() Function
for x in range(6):
    print(x)

#Using the start parameter   
for x in range (2, 6):
    print (x)

#Increment the sequence with 3
for x in range (5, 40, 5):
     print(x) 

#Else in For Loop   
for x in range(4):
    print(x)
else:
    print("finally finishied!")

#Nested Loops 
adj ={"important", "usful", "developer"}
programs ={"python", "database", "java"}
for x in adj:
    for y in  programs:
      print(x, y)



