#day17
#Python Tuples 2
#Check if Item Exists 
thistuple = ("apple","cherry","banana")
if "apple" in thistuple:
    print("yes,'apple' is in the fruits tuple")

#Repeat Item 
thistuple = ("python",)*3
print(thistuple)

 #+ Operator in Tuple 
x = (3,4,5,6)
x = x +(1,2,3)
print(x)

thistuple = ("apple","orange","apple") #Tuple Length
print(len(thistuple))

thislist = [3,4,5,6,"A","B"]  
thistuple = tuple(thislist)
print(thistuple)