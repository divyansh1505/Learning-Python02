name = "Arnavi Darokar"

nameshort = name[0:8]
print(nameshort)

#blank space is counted as 2 i guess 



alphabets = "abcdefghijklmnopqrstuvwxyz"
nameshort1 = alphabets[0:9:4]

print(nameshort1)

# endswith("")

print(name.endswith("okar"))    #output is true 
print(name.endswith("okara"))   #output is false 

str = "Arnvai"
print(len(str)) # Output: 6      

str = "Divyansh"
count = str.count("a")
print(count) # Output: 1

str = "divyansh"
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Divyansh"

str = "harry"
index = str.find("rr")
print(index) # Output: 2

str = "Arnavi"
replaced_string = str.replace("r", "n")
print(replaced_string) # Output: "Annavi"


str = "DiVyAnSh"
print(str.swapcase())