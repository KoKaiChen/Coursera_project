# Guess The Number

# Name: 柯凱程

# URL: https://py2.codeskulptor.org/#user51_s8bFLODFVgzFTPU.py

# all output for the game will be printed in the console
import simplegui
import random
import math

number_range = 100
remaining_guesses = 0
secret_number = 0


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global remaining_guesses, secret_number
    secret_number = random.randrange(0, number_range)
    if number_range == 100:
        remaining_guesses = 7
    elif number_range == 1000:
        remaining_guesses = 10
    print("New game. Range is [0," + str(number_range) + ")")
    print("Number of remaining guesses is " + str(remaining_guesses))
    print


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global secret_number, remaining_guesses, number_range
    number_range = 100
    new_game()


def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global secret_number, remaining_guesses, number_range
    number_range = 1000
    new_game()


def input_guess(guess):
    # main game logic goes here
    global remaining_guesses, secret_number
    if int(guess) == secret_number:
        remaining_guesses -= 1
        print("Guess was " + str(guess))
        print("Number of remaining guesses is " + str(remaining_guesses))
        print
        "Correct!"
        new_game()
        return
    elif remaining_guesses == 0:
        print
        "Game over! No more guess remaining."
        new_game()
        return
    elif int(guess) < secret_number:
        remaining_guesses -= 1
        print("Guess was " + str(guess))
        print("Number of remaining guesses is " + str(remaining_guesses))
        print
        "Higher!"
        return
    elif int(guess) > secret_number:
        remaining_guesses -= 1
        print("Guess was " + str(guess))
        print("Number of remaining guesses is " + str(remaining_guesses))
        print
        "Lower!"
        return


# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter your guess", input_guess, 100)

# call new_game
new_game()
frame.start()

# always remember to check your completed program against the grading rubric
