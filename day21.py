#Python Sets 2
#Get the Length of a Set
thisset = {"apple","orange","banana"} 
print(len(thisset))

 #Remove item
thisset ={"apple","orange","banana",} 
thisset.remove("orange")
print(thisset)

#discard
thisset ={"apple","orange","banana",} 
thisset.discard("apple")
print(thisset)

#The pop() method removes .
thisset ={"apple","orange","banana","grap"}
x= thisset.pop()
print(x)
print(thisset)

#The clear() method empties the list.
thisset={"apple","orange","banana"} 
thisset.clear()
print(thisset)

#The set() Constructor 
thisset= set(("apple","orange","banana")) 
print(thisset)

