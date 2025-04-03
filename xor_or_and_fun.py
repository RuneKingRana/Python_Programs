def XOR(num1, num2):
    return num1 ^ num2

def OR(num1, num2):
    return num1 | num2

def AND(num1, num2):
    return num1 & num2

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
if n1 != 0 and n1 != 1 :
    print("Invalid input!!")
elif n2 != 0 and n2 != 1 :
    print("Invalid input!!")
else:
    print(f"Result of XOR({n1}, {n2}):", XOR(n1, n2))
    print(f"Result of OR({n1}, {n2}):", OR(n1, n2))
    print(f"Result of AND({n1}, {n2}):", AND(n1, n2))

