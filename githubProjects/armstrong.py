
def numcount(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count


def armstrong(num):
    b = num
    a = 0
    r = numcount(num)
    while num > 0:
        digit = num % 10
        a = a + digit ** r
        num = num//10
    if a == b:
        print("Number is a Armstrong number.")
    else:
        print("Number is not a Armstrong number.")


n = int(input('Enter the number:'))
armstrong(n)




