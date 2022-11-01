def palindrome(string):
        rev = string[::-1]
        if string == rev:
                print("It is palindrome.")
        else:
                print("Not a palindrome.")

def symmetry(string):
        l = len(string)
        if (l % 2 == 0):
                h = l//2
        else:
                print('Not symmetric.')
        q = string[0:h]
        w = string[h:]

        if q == w:
                print("String is symmetric")
        else:
                print('Not symmetric.')

strin = input("Enter the string:")
palindrome(strin)
symmetry(strin)









