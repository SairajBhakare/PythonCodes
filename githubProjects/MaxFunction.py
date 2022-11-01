
# Write a python function to find the maximum of 3 given numbers
def maximum(a, b, c):
    return max(a, b, c)


a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
print(maximum(a, b, c))


def max2(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= b and c >= a:
        return c


a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))
print(max2(a, b, c))




