greeting = "Good Morning"

if greeting == "Günaydın":
    print("this is Turkish")
    print("You can speak Turkish")
else:
    print("this is not Turkish")
print("if condition finished")
print()

a = 4
if a>2:
    print("as expected")
else:
    print("check the number")
print()
#Loops
print("-----Loops-----")
num = [1, 2, 3, 4, 5, 6]
for i in num:
    print(i*i)
sumOfNum = 0
for j in range (1, 6):  # range (i,j) -> i to j-1 ///
    print(j)
    sumOfNum = sumOfNum + j
print(sumOfNum)
for l in range (10): # 
    print(l)
print("---------------")
for k in range (1, 5, 2): # like for(i=0,i<5,i+2) in Java
    print(k)