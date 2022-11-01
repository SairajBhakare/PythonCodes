def numcount(num):
    # count = 0
    # while num > 0:
    #   num = num//10
    #   count = count + 1
    # return count
    numstr = str(num)
    leng = len(numstr)
    return leng


def Armstrong(n, m):
    flag = 0
    for i in range(n, m+1):
        j = 0
        c = numcount(i)
        k = i
        while(i > 0):
            digit = i % 10
            j = j + digit**c
            i = i//10
        if k == j:
           print(k)
           flag = 1
    if flag != 1:
        print("No armstrong number present.")


n = int(input("Enter the start of range:"))
m = int(input("Enter the end of range:"))
Armstrong(n, m)
