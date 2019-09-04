#day15
#Python Lists 3 
#List Length
colors =["red","blue","grey","pink"]
print(len(colors))

#Add Items 
colors =["red","blue","grey","pink"]
colors.append("green")
print(colors)

 #To add an item at the specified index, use the insert() method
colors =["red","blue","grey","pink"]
colors.insert(1,"yellow")
print(colors)

 #Remove Item 
colors =["red","blue","grey","pink"]
colors.remove("blue")
print(colors)

#The pop() method removes the specified index.
colors =["red","blue","grey","pink"]
colors.pop()
print(colors)

#The clear() method empties the list.
colors =["red","blue","grey","pink"]
colors.clear()
print(colors)
