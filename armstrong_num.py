n = int(input("Enter a number: "))
digits = len(str(n))
sum = 0
temp = n
while (temp!=0):
    digit = temp % 10
    sum += digit ** digits
    temp //= 10
if (n==sum):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")