import random
print("NUMBER GUESING GAME")
print("Guess a number between 1-9")
chances=0
number=random.randint(1,9)
while chances<5:
    answer=int(input("Enter your guess:"))
    if answer==number:
        print("CONGRATS YOU WON!")
        break
    elif answer<number:
        print("Your guess was too low.")
    else:
        print("Your guess is too high.")
    chances+=1
if not chances<5:
    print("You lose, The number is ",number)