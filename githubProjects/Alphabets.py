def A():
    for i in range(1, 6):
        for j in range(1, 6):
            if(i == 1 and j == 3 or j == 2 and i > 1 or j == 4 and i > 1 or i == 3 and j == 3 ):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print(" ")

def B():
    for i in range(1, 6):
        for j in range(1, 6):
          if(i == 1 and j == 3 or j == 2 and i >= 1 or j == 4 and i >= 1 or i == 3 and j == 3 or i == 5 and j == 3):
                print("*", end=" ")
          else:
                print(" ", end=" ")
        print(" ")

A()
print('\t')
B()
