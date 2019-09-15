#Python Dictionaries 3

#Copy a Dictionary
thisdict  = {
    "huda": "Almutairi",
    "city": "khobar",
    "year": 1997
}
mydict = thisdict.copy()
print(mydict)

#Nested Dictionaries
myFamily = {
    "sister1": {
        "name": "maali",
        "year": "1994",
 },
 "sister2": {
     "name":  "Afrah",
     "year": "1991",
 },
 "sister3": {
     "name":  "Asmaa",
     "year": "1995",
 }
}
print(myFamily)

#The dict() Constructor
thisdict  = dict(name="huda",city="khobar",year= 1997)
print(thisdict)