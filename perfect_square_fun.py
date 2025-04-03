def square(x):
    if x >= 0:
        sr = int(x ** 0.5)
        return (sr * sr == x)
    return False

x = int(input("Enter a number: "))
if square(x):
    print(f"{x} is a perfect square.")
else:
    print(f"{x} is not a perfect square.")
