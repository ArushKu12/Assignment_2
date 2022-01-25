#Question 6
a=int(input("Enter first side="))
b=int(input("Enter second side="))
c=int(input("Enter third side="))
if c>=a+b :
 print("NO")
elif b>=a+c :
 print("NO")
elif a>=b+c :
 print("NO")
else :
 print("YES")
