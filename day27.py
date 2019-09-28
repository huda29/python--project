#Conditional Statements Python If and Else
#if statment 
a=33
b=200
if b > a:
    print("b is greater than a")
#Elif 
a=33
b=33
if b > a:
    print("b is greater than a")
elif b==a:
    print("a and b are equal")    
# else
a=200
b=33
if b > a:
    print("b is greater than a")
elif b==a:
    print("a and b are equal")
else:
    print("a is greater than b") 

#Short Hand If
# One line if statement 
a=200
b=33
if a > b: print("a is greater than b")

# One line if else statement
a =20
b = 10
print("a") if a > b else print("b")
#One line if else statement, with 3 conditions
a= 330
b= 330
print("a") if a > b else print("=") if a==b else print ("b")

#And
a= 200
b= 33
c= 500
if a > b and c > a:
    print("booth condations are true")

#or
a= 200
b= 33
c= 500
if a > b or a > c:
    print("At least one of the condations is True")

#Nested If    
x=41
if x > 10:
    print("Above ten,")
if x > 20:
    print("and also above 20!")
else:
    print("but not above 20.")         


