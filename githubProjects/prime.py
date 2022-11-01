
# 4)Write a python function to check if a number is prime

def prime(v):
    if v == 1:
        print("Number is neither prime nor composite")
    if v == 2 or v == 3:
        print("Number is prime.")
    if v != 1 or v != 2 or v != 3:
        for i in range(2, v//2+1):
            if v % i == 0:
                print("Number is composite")
                break
            else:
                print("Number is prime")
                break


j = int(input("Enter the number:"))
prime(j)

