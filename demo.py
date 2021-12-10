print("Hello world")
# Started to work
a = 3
Str = "hi bluecodersolutions"
print(Str)
print(a)

b, c, d = 5, 6.5, "great"

print("{} {}".format("Value is", c)) # farklı data type concatenate etmek için
print(type(c))
print(type(d))
print("This is "+Str) # aynı data type olduğundan + kullanılabilir
print(a+b) # a+b=8
print("{}{}".format(a,b)) # 35

valueList = [5, "ziya", 32, "mehmet", 69]
print(valueList[1]) # ziya
print(valueList[-1]) # 69
print(valueList[1:3]) # ['ziya', 32]
valueList.insert(3, 'ömer')
print(valueList)
valueList.append("anıl")
print(valueList)
del valueList[6]
print("{} {}".format("after del", valueList))

#Tuple
valueTuple = (1, 6, "zehra" , "azra")
print(valueTuple[2])

#Dictionary
dicti = {1: 5, 2: "ziya", "a": "hamed", "b": "Blue Coder"}
print(dicti['b']) # Blue Coder
dicti["c"] = "mehmet"
print(dicti)

