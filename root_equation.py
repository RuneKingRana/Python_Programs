from math import sqrt
print("For the equation: ax² + bx + c = 0 ")
a = float (input("Enter coefficient for a: "))
b = float (input("Enter coefficient for b: "))
c = float (input("Enter coefficient for c: "))
if a == 0 :
    print("Coefficient of a can't be 0.")
else:
    print(f"For the equation: {a}x² + {b}x + {c} = 0 ")
    des = b**2 + 4*a*c
    r1 = (-b + sqrt(des)) / (2*a)
    r2 = (-b - sqrt(des)) / (2*a)
    print(f"The two roots are: {r1} , {r2}")
