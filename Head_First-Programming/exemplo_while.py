from random import randint
secret = randint(1, 10)
print("Welcome!")
guess = 0
while guess != secret:
    guess = int(input("Guess the number: "))
    if guess > secret:
            print("Too High!")
    elif guess < secret:
        print("Too Low!")   
print("You Win")