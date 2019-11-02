# week 10
#Python String Formatting 2 

quantity = 3
itemno = 567
price = 50

myorder = 'I want {0} pieces  of item number {1} for {2:.2f} dollars.'
print(myorder.format(quantity,itemno, price ))

# if you want to refer to the same value more than once, use the index number. 
name = "Huda"
age = 22
text = "My name is {1}.{1} is {0} years old."
print(text.format(age, name))

