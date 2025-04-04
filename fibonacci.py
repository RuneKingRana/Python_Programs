n = int(input("Enter the length: "))
a,b = 0,1
print("The fibonacci series: ",end ="")
for i in range (n):
    print(a,end =" ")
    a,b = b,a+b