# rajkumar.py
import random

print (" Hello welcome to Guess Game")

smaller = int(input("Enter the Smaller number: "))
larger = int(input("Enter the Larger number: "))

myNumber = random.randint(smaller, larger)

count=0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if userNumber < myNumber:
        print("Too Small!")
    elif userNumber > myNumber:
        print("Too Large!")
    else:
        print("Congratulations! You've got it in", count, "tries!")
        break
