#Python Functions 2 
#Passing a List as a Parameter 
def my_function(data):    
    for x in data:
        print(x)
information = ["name", "city", "phone"] 

my_function(information)

#Return Values
def my_function(x):
   return 8 * x 

print(my_function(4))
print(my_function(3))
print(my_function(2))

#Keyword Arguments 
def my_function(java, php, python):
    print("I am very exited to learn  " + python)
my_function(java ="language", php="connection", python="programs")

#Arbitrary Arguments 
def my_function(*programs):
    print("the important programs " + programs[1])

my_function("java", "php", "python")

#Recursion 
def tri_Recursion(F):
    if (F>0):
        result = F+tri_Recursion(F-1)
        print(result)
    else:
         result = 0
    return result
print("\n\nRecursion example results")
tri_Recursion(6)
