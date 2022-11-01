a = input("Enter any character:")
b = int(input("Enter number of rows:"))
for x in range(1, b+1):
    for y in range(x):
        print(a, end=" ")
    print(" ")
for x in range(b-1, 0, -1):
    for y in range(x):
        print(a, end=" ")
    print(" ")
