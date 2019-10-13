# Python Arrays 2
#Looping Array Elements

information = ["name", "email", "city" ]
for x in information:
    print(x)
#Adding Array Elements
information = ["name", "email", "city" ]
information.append("phone")
print(information)

#Removing Array Elements 
information = ["name", "email", "city" ]
information.pop(1)
print(information)
#You can also use the remov()
information = ["name", "email", "city" ]
information.remove("name")
print(information)
