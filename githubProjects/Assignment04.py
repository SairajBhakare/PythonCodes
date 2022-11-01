
# Program to print numbers between starting and ending number


a = int(input('Enter the starting number:'))
b = int(input("Enter the ending number:"))
print(f'The numbers in between {a} and {b} are:')
for x in range(a+1, b):
    print(x)
