'''
pattern -   *               *
            * *           * *
            * * *       * * *
            * * * *   * * * *
            * * * * * * * * *
'''

n = int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(1,(n-i-1)*2):
        print(" ",end=" ")
    if (i != n-1):
        print("*", end=" ")
    for j in range(1,i+1):
        print("*", end=" ")
    print()