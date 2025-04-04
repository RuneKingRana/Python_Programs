'''
pattern -   *       *
              *   *
                *
              *   *
            *       *
'''

n = int(input("Enter the number of rows: "))
if (n%2) == 0:
    print("Enter a odd nuber of row for symmetric pattern.")
else:
    for i in range(n):
        for j in range(n):
            if (i == j) or (i+j == n-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()