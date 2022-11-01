# Write a python function to generate multiplication table of a given number

n = int(input("Enter the number:"))
def multable():
    for x in range(1,11):
       print(n*x)
multable()