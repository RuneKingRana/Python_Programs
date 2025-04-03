original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, original_list))
odd_numbers = list(filter(lambda x: x % 2 != 0, original_list))

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)

