#day14
#Python Lists 2 
informations =["ID","Phone","email","age"] 
print(informations[1:3])

 #Check if Item Exists 
informations =["ID","Phone","email","age"] 
if "email" in informations:
  print("yes,'email' is in the informations list")

#Repeat Item in List 
informations =["ID"] *3
print(informations)

# + Operator in List To add 2 lists or more into one list. 
grade1 =["9.5","7.3","4.4","8.8"]
grade2 =["10","3","6","9"]
grade3 = grade1 + grade2
print(grade3)