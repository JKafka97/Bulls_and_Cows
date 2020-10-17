import random


def greets():
    print('''Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game. 
Enter a number''')


def random_number():
    number = set()
    while len(number) < 3:
        number.add(random.randrange(0, 10))
    while len(number) < 4:
        number.add(random.randrange(1, 10))
    complete_random_number = ""
    for num in number:
        complete_random_number += str(num)
    return complete_random_number


def input_control():
    while True:
        my_input_number = input()
        if len(my_input_number) == 4 and my_input_number.isdigit():
            return my_input_number
        else:
            print("Your number has to be four-digit number")


def bulls_cows_control():
    guess = 0
    my_random_number = random_number()
    while True:
        bulls_cows = {"bulls": 0, "cows": 0}
        my_input_number = input_control()
        for index, value in enumerate(my_random_number):
            if value == my_input_number[index]:
                bulls_cows["bulls"] += 1
            elif value in my_input_number:
                bulls_cows["cows"] += 1
        guess += 1
        bull_s, cow_s = bulls_multiple(bulls_cows)
        if bulls_cows["bulls"] == 4:
            return guess
        print("{} bull{}, {} cow{}".format(bulls_cows["bulls"], bull_s, bulls_cows["cows"], cow_s))


def bulls_multiple(bulls_cows):
    bull_s, cow_s = "s", "s"
    if bulls_cows["bulls"] == 1:
        bull_s = ""
    if bulls_cows["cows"] == 1:
        cow_s = ""
    return bull_s, cow_s


def guess_multiple(guess):
    multi = "" if guess == 1 else "es"
    return multi


def correct_ans(guess):
    multi = guess_multiple(guess)
    print("Correct, you've guessed the right number in {} guess{}!".format(guess, multi))


def ans_write(guess):
    file = open('score.txt', 'a+')
    file.write("{},".format(str(guess)))
    file.seek(0)
    score = ((file.read()).strip(",")).split(",")
    my_sum = 0
    for numbers in score:
        my_sum += int(numbers)
    average = my_sum / len(score)
    print("Average score is {}".format(round(average)))


def calculate_result():
    greets()
    my_ans = bulls_cows_control()
    guess_multiple(guess=my_ans)
    correct_ans(guess=my_ans)
    ans_write(guess=my_ans)


calculate_result()
