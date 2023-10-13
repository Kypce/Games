# **NOTE**: I implemented the algorithmic decision making for the computer (Alg_ComputerPlayer) but had trouble downloading the numphy header file.
#           I left the code in but was not able to test it so I do not know if it works, currently the program has the random decision making active
#           for the computer (Rand_ComputerPlayer). I also have a comment in PlayGame() which line would need to be changed to choose between these options.

#%% 
from functools import total_ordering
from random import randint
import numpy as np
#note: x=randint(0, 10) will generate a random integer x and 0<=x<=10

# %% Asks/Gets valid user input
def HumanPlayer(GameRecord):
    valid_entries = ["r", "rock", "p", "paper", "s", "scissors", "g", "game", "q", "quit"]
    user_choice = input("Please type either r (rock), p (paper), s (scissors), g (game), or q (quit): ")
    print("g (game) will view the GameRecords while q (quit) will quit out of the application")
    if user_choice not in valid_entries:
        print("Input was not valid")
        print()
        return HumanPlayer(GameRecord)
    print()
    return user_choice 

# %% RANDOMLY chooses computer's choice
def Rand_ComputerPlayer(GameRecord):
    rand = randint(0,2)
    if rand == 0:
        computer_choice = "rock"
    elif rand == 1:
        computer_choice = "paper"
    elif rand == 2:
        computer_choice = "scissors"
    else:
        computer_choice = "error"
    return computer_choice

# %% ALGORITHMICLY chooses computer's choice
def Alg_ComputerPlayer(GameRecord):
    totals = []
    for result in GameRecord[0]:
        if(result == "rock"):
            totals[0] += 1
            totals[3] += 1
        elif result == "paper":
            totals[1] += 1
            totals[3] += 1
        elif result == "scissors":
            totals[2] += 1
            totals[3] += 1
        else:
            Rand_ComputerPlayer(GameRecord)
    frequencies = []
    frequencies[0] = totals[0] / totals[3]
    frequencies[1] = totals[1] / totals[3]
    frequencies[2] = totals[2] / totals[3]
    draw = np.random.choice(["rock", "paper", "scissors"], 1, p = [frequencies[0], frequencies[1], frequencies[2]])[0]
    return draw


# %% Judges who wins between user and computer choices
# 0 signifies tie, 1 signifies computer wins, and 2 signifies user wins
def Judge(ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    if ChoiceOfComputerPlayer == ChoiceOfHumanPlayer:
        return 0
    elif ChoiceOfHumanPlayer == "rock":
        if ChoiceOfComputerPlayer == "paper":
            return 1
        else:
            return 2
    elif ChoiceOfHumanPlayer == "paper":
        if ChoiceOfComputerPlayer == "scissors":
            return 1
        else:
            return 2
    elif ChoiceOfHumanPlayer == "scissors":
        if ChoiceOfComputerPlayer == "rock":
            return 1
        else:
            return 2
    else:
        return -1

# %% This is changing the shortand inputs to the full name for display/recording
def user_input_update(ChoiceOfHumanPlayer):
    if ChoiceOfHumanPlayer == "r":
        ChoiceOfHumanPlayer = "rock"
    elif ChoiceOfHumanPlayer == "p":
        ChoiceOfHumanPlayer = "paper"
    elif ChoiceOfHumanPlayer == "s":
        ChoiceOfHumanPlayer = "scissors"
    else:
        ChoiceOfHumanPlayer = ChoiceOfHumanPlayer
    return ChoiceOfHumanPlayer


# %% Prints the outcome of a single game based on user and computer choices
def PrintOutcome(Outcome, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer):
    print("----------Outcome----------")
    if Outcome == 0:
        print("It was a tie!")
    elif Outcome == 1:
        print("The Computer Won!")
    elif Outcome == 2:
        print("The Human Won!")
    else:
        print("An error occurred somewhere")
    print("Computer chose:", ChoiceOfComputerPlayer)
    print("Human chose:", ChoiceOfHumanPlayer)
    print("---------------------------")
    print()

# %% Updates GameRecord with results and choices of game just played
def UpdateGameRecord(GameRecord, ChoiceOfComputerPlayer, ChoiceOfHumanPlayer, Outcome):
    GameRecord[0].append(ChoiceOfHumanPlayer)
    GameRecord[1].append(ChoiceOfComputerPlayer)
    GameRecord[2].append(Outcome)

# %% Prints the full GameRecord of all games played
def PrintGameRecord(GameRecord):
    user_wins = 0
    comp_wins = 0
    ties = 0
    total_games = 0
    for result in GameRecord[2]:
        if result == 0:
            ties += 1
            total_games += 1
        elif result == 1:
            comp_wins += 1
            total_games += 1
        else:
            user_wins += 1
            total_games += 1
    print("-------Record of the Game-------")
    print("The number of round(s) is", total_games)
    print("User won", user_wins, "round(s)")
    print("Computer won", comp_wins, "round(s)")
    print("There have been", ties, "tie(s)")
    print("User | Computer -- Choices")
    for x in range(len(GameRecord[0])):
        print(GameRecord[0][x], "|", GameRecord[1][x])
    print()

# %% Calls "game funcions" 
def PlayGame():
    user_record  = []
    comp_record = []
    outcome_record = []
    GameRecord = [user_record, comp_record, outcome_record]
    while True:
        user_choice = HumanPlayer(GameRecord)
        if user_choice == "g" or user_choice == "game":
            PrintGameRecord(GameRecord)
        elif user_choice == "q" or user_choice == "quit":
            break
        else:
            user_choice = user_input_update(user_choice)
            # Line below is line to change to change from random to algorithmic choice for computer
            comp_choice = Rand_ComputerPlayer(GameRecord)
            outcome = Judge(comp_choice, user_choice)
            UpdateGameRecord(GameRecord, comp_choice, user_choice, outcome)
            PrintOutcome(outcome, comp_choice, user_choice)
    print("Thank you for playing!")
    print()
        
# %% do not modify anything below
if __name__ == '__main__':
    print()
    print("Welcome to Rock, Paper, Scissors!")
    PlayGame()
