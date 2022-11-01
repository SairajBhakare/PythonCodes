# Write a python function to print even numbers from a given list

ilist = [12,34,45,56,67,78,89,90]
def evenadd():
    k = 0
    for x in ilist:
        if(x % 2 == 0):
          k = k + x
    print(k)
ilist = [12,34,45,56,67,78,89,90]
evenadd()
