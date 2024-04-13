# Rock-paper-scissors-lizard-Spock mini-project

#URL:https://py2.codeskulptor.org/#user51_yrigHFukNxnwWE0.py

'''
Converting strings into interger and Compete with 
computer by using operators.

Practice using def(),random() functions, if/else keyword, and simple operators
'''

# The idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random


# helper functions
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "error"


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "error"


def rpsls(player_choice):
    print("Player chooses " + player_choice)
    # print out the message for the player's choice

    player_number = name_to_number(player_choice)
    # convert the player's choice to player_number using the function name_to_number()

    comp_number = random.randrange(0, 5)
    # compute random guess for comp_number using random.randrange()

    comp_choice = number_to_name(comp_number)
    # convert comp_number to comp_choice using the function number_to_name()

    print("Computer chooses " + comp_choice)
    # print out the message for computer's choice

    result = player_number - comp_number
    # compute difference of comp_number and player_number modulo five

    if result == 1 or result == 2 or result == -3 or result == -4:
        print("Player wins!")
        print()
    elif result == -1 or result == -2 or result == 3 or result == 4:
        print("Computer wins!")
        print()
    else:
        print("Player and computer tie!")
        print()
    # use if/elif/else to determine winner, print winner message

    print
    # print a blank line to separate consecutive games


# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

