def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
        print(num % 2, end = ' ')

if __name__ == '__main__':
    n=int(input("Enter a number: "))
    print("The binary equivalent is:")
    DecimalToBinary(n)
