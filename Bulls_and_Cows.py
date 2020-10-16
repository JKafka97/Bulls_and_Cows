import random

print('''Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game. 
Enter a number''')


def random_number():
    number = set()
    while len(number) < 4:
        number.add(random.randrange(1, 10))
    complete_random_number = ""
    for num in number:
        complete_random_number += str(num)
    return complete_random_number


def input_control(input_number):
    if len(input_number) != 4 or not input_number.isdigit():
        print("Your number has to be four-digit number")
    else:
        return input_number


def bulls_cows_control(bull_s, cow_s):
    guess = 1
    bulls_cows = {"bulls": 0, "cows": 0}
    while bulls_cows["bulls"] != 4 and bulls_cows["cows"] != 4:
        input_number = input()
        input_control(input_number)
        n = 0
        for bulls in random_number():
            if bulls == input_number[n]:
                bulls_cows["bulls"] += 1
            if bulls in input_number:
                bulls_cows["cows"] += 1
            n += 1
        guess += 1
        print("{} bull{}, {} cow{}".format(bulls_cows["bulls"], bull_s, bulls_cows["cows"], cow_s))
    return bulls_cows


def guess_multiple(guess):

    if guess == 1:
        multi = ""
    else:
        multi = "es"
    return multi


def correct_ans(bulls_cows, guess, multi):
    if bulls_cows["bulls"] == 4 and bulls_cows["cows"] == 4:
        print("Correct, you've guessed the right number in {} guess{}!".format(guess, multi))


def bulls_multiple(bulls_cows):
    bull_s, cow_s = "s", "s"
    if bulls_cows["bulls"] == 1 and bulls_cows["cows"] == 1:
        bull_s, cow_s = "", ""
    if bulls_cows["bulls"] == 1:
        bull_s = ""
    if bulls_cows["cows"] == 1:
        cow_s = ""
    return bull_s, cow_s


def ans_write(guess):
    file = open('score.txt', 'a+')
    file.write("{},".format(str(guess)))
    file.seek(0)
    score = ((file.read()).strip(",")).split(",")
    my_sum = 0
    for numbers in score:
        my_sum += int(numbers)
    average = my_sum / len(score)
    print("Average score is {}".format(average))
