
# Program to find factorial of a number
k = int(input('Enter the number:'))
i = 1
for x in range(1, k+1):
    i = i*x
print(f"The factorial of {k} is {i}")


# Alternate method


def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial(n-1)


num = int(input("Enter the number:"))
print(f"The factorial of {num} is", factorial(num))
    



