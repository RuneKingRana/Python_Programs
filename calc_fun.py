def calc(m,n,c):
    if c == "+":
        print ("your answer is:",(m + n))
    elif c == "-":
        print ("your answer is:",(m - n))
    elif c == "*":
        print("your answer is:",(m * n))
    elif c == "/":
        print("your answer is:",(m / n))
    else :
     print ("Invalid Input!!")

m = int(input("Enter first number: "))
n = int(input("Enter second number: "))
c = input("Enter operation: ")
calc(m,n,c)
