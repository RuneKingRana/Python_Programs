def leapyear(n):
    if (n%4==0 and n%100!=0 or n%400==0):
        print(f"{n} is a leap year.")
    else:
        print(f"{n} isn't a leap year.")
    
n=int(input("Enter a year:"))
leapyear(n)