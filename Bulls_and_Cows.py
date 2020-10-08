import random

print('''Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game. 
Enter a number''')

#random_number
number = set()
while len(number) < 4:
    number.add(random.randrange(1, 10))
random_number = ""
for num in number:
    random_number += str(num)
print(random_number)

#game_loop
guess = 1
while True:
    bulls_cows = {"bulls": 0, "cows": 0}
    input_number = input()
    if len(input_number) != 4:
        print("Your number has to be four-digit")
        continue
    n = 0
    for bulls in random_number:
        if bulls == input_number[n]:
            bulls_cows["bulls"] += 1
        if bulls in input_number:
            bulls_cows["cows"] += 1
        n += 1
    if bulls_cows["bulls"] == 4 and bulls_cows["cows"] == 4:
        print("Correct, you've guessed the right number in {} guesses!".format(guess))
        break
    bull_s, cow_s = "s", "s"
    template = "{} bull{}, {} cow{}"
    if bulls_cows["bulls"] == 1 and bulls_cows["cows"] == 1:
        bull_s, cow_s = "", ""
    if bulls_cows["bulls"] == 1:
        bull_s = ""
    if bulls_cows["cows"] == 1:
        cow_s = ""
    print(template.format(bulls_cows["bulls"], bull_s, bulls_cows["cows"], cow_s))
    guess += 1
