import random

print("Hi there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")
print("Enter a number")
#random_number
number = set()
while len(number) < 4:
    number.add(random.randrange(1, 10))
random_number = ""
for num in number:
    random_number += str(num)
print(random_number)
#game_loop
bulls_cows = {"bulls": 0, "cows": 0}
guess = 1
while bulls_cows:
    input_number = input()
    if len(input_number) != 4:
        print("Your number has to be four-digit")
        continue
    n = 0
    for bulls in str(random_number):
        if bulls == input_number[n]:
            bulls_cows["bulls"] += 1
        if bulls in input_number[n]:
            bulls_cows["cows"] += 1
        n += 1
    if bulls_cows["bulls"] == 4 and bulls_cows["cows"] == 4:
        print("Correct, you've guessed the right number in {} guesses!".format(guess))
        break
    else:
        print(bulls_cows)
        guess += 1
        bulls_cows = {"bulls": 0, "cows": 0}
        continue
