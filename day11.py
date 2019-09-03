#day 11 
#Logical Operators
x=5
print(x>3 or x<4) # returns true because on of the condation are true 

#Python Identity Operator
x={"apple" , "banana"}
y={"apple" , "banana"}
z=x

print(x is not z) # returns false because z is the same object as x

print(x is not y) # returns true because x is not  the same object as y

print(x !=y) # returns false because x is not equal to y

#Python Membership Operators
x={"apple" , "banana"}
print("banana" in x) #returns true because a sequence with the banana is in the list
