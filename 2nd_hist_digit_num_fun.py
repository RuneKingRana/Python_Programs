def second(number):
    number = abs(number)
    unique_digits = sorted(set(int(digit) for digit in str(number)), reverse=True)
    if len(unique_digits) < 2:
        return "No second-highest digit"
    return unique_digits[1]


user_input = int(input("Enter an integer: "))
print("Second highest digit:", second(user_input))
