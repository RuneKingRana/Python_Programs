'''
series - 1 + 1/2! - 1/3! + 1/4! -1/5! + ...1/n!
'''

def fact(n):
    if (n==0) or (n==1):
        return 1
    else:
        return n * fact(n-1)

n = int(input("Enter a number: "))
even = 0
odd = 0
for i in range (2, n+1):
    d = fact(i)
    if (i % 2 == 0):
        even += (1/d)
    else:
        odd += (1/d)
result = 1 + even - odd
print("Result: ", result)