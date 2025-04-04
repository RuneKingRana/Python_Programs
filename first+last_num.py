n = int(input("Enter a number: "))
last = n%10
first = n
while(first>=10):
    first//=10
sum = first + last
print("The sum of the first and last digit is: ",sum)