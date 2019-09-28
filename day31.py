#Python Functions 
#Creating a Function
# Calling a Function 
def my_function():
    print("hello from a function")
my_function()
#Parameters 
def my_function(fname):
    print(fname + "language")
my_function("python")  
my_function("c++") 
my_function("java") 
#Default Parameter Value
def my_function(language = "no rway"):
    print(" Iam excited to learn" + language)   
my_function("python")  
my_function("c++") 
my_function()
my_function("java")


