def even(list):
    for i in list:
        if i%2 == 0:
            print(i)


# input_str = input("Enter the elements of list separated by space:")
# input_list = input_str.split()
# print("The input list is", input_list)
# for x in range(len(input_list)):
#     input_list[x] = int(input_list[x])
# even(input_list)

lst = []

n = int(input("Enter the number of elements in the list:"))
for i in range(0,n):
    ele = int(input("Enter the element:"))
    lst.append(ele)
print(lst)
even(lst)






