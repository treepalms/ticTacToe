# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import random

free_spaces = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

winner = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
          ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
          ['1', '5', '9'], ['3', '5', '7']]

tic_tac_toe_board = {'1': '-', '2': '-', '3': '-',
                      '4': '-', '5': '-', '6': '-',
                      '7': '-', '8': '-', '9': '-'}

user_all_inputs = []
computer_all_inputs = []
user_won = False
computer_won = False
game_end = False

def print_board(board):
    print(board['1'], board['2'], board['3'])
    print(board['4'], board['5'], board['6'])
    print(board['7'], board['8'], board['9'])

def check_user_win():
    global game_end
    global user_won
    for i in range(len(winner)):
        winning_sets = set(winner[i])
        if all(item in user_all_inputs for item in winning_sets):
            user_won = True
    if user_won == True:
        print("You won!")
        game_end = True
        check_game_end()
    else:
        check_tie()
        if game_end == False:
            computers_turn()

def check_computer_win():
    global game_end
    global computer_won
    for i in range(len(winner)):
        winning_sets = set(winner[i])
        if all(item in computer_all_inputs for item in winning_sets):
            computer_won = True
    if computer_won == True:
        print("The computer won!")
        game_end = True
        check_game_end()
    else:
        check_tie()
        if game_end == False:
            users_turn()

def check_tie():
    global game_end
    if len(free_spaces) == 0:
        if user_won == False and computer_won == False:
            game_end = True
            print("It's a tie!")
            check_game_end()

def check_game_end():
    if game_end == True:
        play_again = input("Play again? Enter an option — yes, no: ")
        if play_again == "yes":
            reset()
        elif play_again == "no":
            sys.exit()
        else:
            print("Sorry, an error occurred. Did you enter your option correctly?")
            check_game_end()

def reset():
    global free_spaces
    global user_won
    global computer_won
    global game_end
    global user_all_inputs
    global computer_all_inputs
    global tic_tac_toe_board
    free_spaces = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    user_won = False
    computer_won = False
    game_end = False
    user_all_inputs = []
    computer_all_inputs = []
    tic_tac_toe_board = {'1': '-', '2': '-', '3': '-',
                      '4': '-', '5': '-', '6': '-',
                      '7': '-', '8': '-', '9': '-'}
    game_start()

def game_start():
    global user_playing_symbol
    global computer_playing_symbol
    while True:
        coin_flip = ['heads', 'tails']
        coin_flip_outcome = random.choice(coin_flip)
        user_prediction = input("Let's flip a coin! The one who wins starts first. Enter an option — heads, tails: ")
        if user_prediction in coin_flip:
            if user_prediction == 'heads':
                computer_prediction = 'tails'
            else:
                computer_prediction = 'heads'
            print("You chose", user_prediction)
            print("The computer chose", computer_prediction)
            if user_prediction == coin_flip_outcome:
                user_playing_symbol = 'X'
                computer_playing_symbol = 'O'
                print("You won! You will start the Tic-Tac-Toe game as X, while the computer will go second as O.")
                users_turn()
            else:
                user_playing_symbol = 'O'
                computer_playing_symbol = 'X'
                print("The computer won! The computer will start the Tic-Tac-Toe game as X, while you will go second as O.")
                computers_turn()
        else:
            print("Sorry, an error occurred. Did you enter your option correctly?")

def users_turn():
    user_input = input("Choose one of the options: ")
    if user_input not in free_spaces:
        print("Sorry, an error occurred. Please ensure that an unoccupied number is entered.")
        users_turn()
    else:
        tic_tac_toe_board[user_input] = user_playing_symbol
        user_all_inputs.append(user_input)
        print("")
        print_board(tic_tac_toe_board)
        print("")
        free_spaces.remove(user_input)
        check_user_win()

def computers_turn():
    computer_input = random.choice(free_spaces)
    tic_tac_toe_board[computer_input] = computer_playing_symbol
    computer_all_inputs.append(computer_input)
    print("")
    print_board(tic_tac_toe_board)
    print("")
    free_spaces.remove(computer_input)
    check_computer_win()

game_start()