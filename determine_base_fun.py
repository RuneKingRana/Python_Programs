def determine_base(number_str):
    max_digit = max(int(digit) for digit in number_str)

    if max_digit >= 10:
        return "Invalid number for bases up to 10."
    return max_digit + 1

number_str = input("Enter a number: ")
print("The smallest base for the number is:", determine_base(number_str))
