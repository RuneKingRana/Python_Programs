def sum(x, y):
    even = odd = 0
    for n in range (x , y+1):
        if n % 2 == 0 :
            even += n
        else :
            odd += n
    return even , odd

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
if start >= end:
    print("Start range should be less then end.")
else:
    even_sum, odd_sum = sum(start,end)
    print(f"Sum of even numbers from {start} to {end} : ", even_sum)
    print(f"Sum of odd numbers from {start} to {end} : ", odd_sum)