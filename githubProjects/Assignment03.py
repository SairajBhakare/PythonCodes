# Program to print months from Jan to Dec using for loop
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
c = int(input('Do you want to display months(1/0)'))
while c == 1:
    for x in months:
        print(x)
    break

print("\n")
