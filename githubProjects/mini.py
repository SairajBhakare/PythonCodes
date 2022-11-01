# The Hangman game
import random

# name = input("Enter your name:")
# print(f"Hi {name} let's play a game.")
words = ["maximum","victory","play","work","quality","adapt","reason","spectacular","sole","secret","change",
         "challenge","check","choice","champion","dog","apple","basket","book","bench","brother",
         "elegant","glory","humble","peace","keep","close","stop","health","live","lemon","lost","magnificent"]
secret = random.choice(words)
slist = list(secret)
print(slist)
n = len(secret)
for j in range(n):
    print("_")
for i in slist:
    a = input("Guess the letter:")
    if a == i:
       print(a)



