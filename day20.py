#Empty Set.
thisset ={}
print(thisset)
#Create a Set. 
programing ={"java","php","mysql","python"}
print(programing)

thisset={"java" ,"php", 1, 2, 1, 3}
print(thisset)
 #Access Items 
thisset={"java","php","mysql","python"} 
for x in thisset:
    print(x)
#add
programing ={"java","php","mysql","python"}
programing.add("C++")
print(programing)  
#ubdate
programing ={"java","php","mysql","python"}
programing.update({"C++", "Html","oracal","R"})
print(programing)  