import random

print("Hi, welcome to my game.\n")

print("I'll think of a number and you will try to guess it.\n")

correct_number = random.randint(1, 5)
got_it_right = False
user_guess = 0

while(got_it_right == False):
    print("Please guess my number between 1 and 5.\n")
    user_guess = int(input())
    got_it_right = (user_guess == correct_number)

    if(got_it_right == False):
        print("That's not it! Try again!")

print(f"You got it right! The number was {correct_number}!")
