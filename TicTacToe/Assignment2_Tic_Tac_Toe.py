"""
Course: Introduction to Python Programming
Name: Matthew Class
"""
#%%
def author():
    return "Matthew Class"

    '''
    return your name
    '''

#%%
import random
import copy
import re

#%%
def DrawBoard(Board):
    for i in range(0, 3):
        if i != 0:
            print()
            print("- + - + -")
        for j in range(0,3):
            if j != 2:
               print(Board[i][j], end=' | ')
            else:
               print(Board[i][j],end='')
            
    '''
    Parameter: Board is a 3x3 matrix (a nested list).
    Return: None
    Description: this function prints the chess board    
    hint: Board[i][j] is ' ' or 'X' or 'O' in row-i and col-j
          use print function
    '''

#%% 
def IsSpaceFree(Board, i ,j):
    i = int(i) - 1
    j = int(j) - 1
    if ((i != 0) and (i != 1) and (i != 2)):
        print("Invalid entry. Please enter either 1, 2, or 3 for a row.")
        print()
        return False
    if ((j != 0) and (j != 1) and (j != 2)):
        print("Invalid entry. Please enter either 1, 2, or 3 for a column.")
        print()
        return False

    if(Board[int(j)][int(i)] == ' '):
            return True
    else:
        return False

    '''
    Parameters: Board is the game board, a 3x3 matrix
                i is the row index, j is the col index
    Return: True or False
    Description: 
        return True  if Board[i][j] is empty ' '
        return False if Board[i][j] is not empty
        return False if i or j is invalid (e.g. i = -1 or 100)
    '''

#%%
def GetNumberOfChessPieces(Board):
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if Board[i][j] != ' ':
                count = count + 1
    return count

    '''
    Parameters: Board is the game board, a 3x3 matrix
    Return: the number of chess piceces on Board
            i.e. the total number of 'X' and 'O'
    hint: define a counter and use a nested for loop, like this
          for i in 0 to 3
              for j in 0 to 3
                  add one to the counter if Board[i][j] is not empty
    '''

#%%
def IsBoardFull(Board):
    count = GetNumberOfChessPieces(Board)
    if count == 9:
        return True
    else:
        return False

    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is fully occupied
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''

#%%
def IsBoardEmpy(Board):
    count = GetNumberOfChessPieces(Board)
    if count == 0:
        return True
    else:
        return False

    '''
    Parameter: Board is the game board, a 3x3 matrix
    Return: True or False
    Description: 
        return True if the Board is empty
        return False otherwise 
    hint: use GetNumberOfChessPieces
    '''

#%%
def UpdateBoard(Board, Tag, Choice):
    row = Choice[0]
    col = Choice[1]
    Board[int(row)][int(col)] = Tag 

    '''
    Parameters: 
        Board is the game board, a 3x3 matrix
        Tag is 'O' or 'X'
        Choice is a tuple (row, col) from HumanPlayer or ComputerPlayer
    Return: None
    Description: 
         Update the Board after a player makes a choice
         Set an element of the Board to Tag
    '''

#%%
def HumanPlayer(Tag, Board):
    while True:
        print("Please enter where on the board you would like to put your tag")
        userRow = input("Row:")
        userCol = input("Column:")
        freeSpace = IsSpaceFree(Board, userRow, userCol)
        if freeSpace == False:
            print("This spot is already taken. Please try another spot.")
        userRow = int(userRow) - 1
        userCol = int(userCol) - 1
        if freeSpace == True:
            position = (userCol, userRow)
        else:
            print("Computer you picked a taken space, please try again.")
        if freeSpace == True:
            return position

    '''
    Parameters:        
        Tag is 'X' or 'O'. If Tag is 'X': HumanPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfHumanPlayer, it is a tuple (row, col)
    Description:
        This function will NOT return until it gets a valid input from the user
    Attention:
        Board is NOT modified in this function
    hint: 
        the user needs to input row-index and col-index, where a new chess will be placed
        use int() to convert string to int
        use try-except to handle exceptions if the user inputs some random string
        if (row, col) has been occupied, then ask the user to choose another spot
        if (row, col) is invalid, then ask the user to choose a valid spot
    '''

#%%
def ComputerPlayer(Tag, Board):
    while True:
        row = random.randint(1,3)
        col = random.randint(1,3)
        freeSpace = IsSpaceFree(Board, row, col)
        if freeSpace == True:
            position = (col -1 , row -1)
            return position

    '''
    Parameters:
        Tag is 'X' or 'O'. If Tag is 'X': ComputerPlayer goes first    
        Board is the game board, a 3x3 matrix
    Return: ChoiceOfComputerPlayer, it is a tuple (row, col)   
    Description:
        ComputerPlayer will choose an empty spot on the board
        a random strategy in a while loop:
            (1) randomly choose a spot on the Board
            (2) if the spot is empty then return the choice (row, col)
            (3) if it is not empty then go to (1)
    Attention:
        Board is NOT modified in this function
    '''

#%%
def Judge(Board):
    # Return value meaning: 1 ('X' player wins), 2 ('O' player wins), 3 (Tie), 0 (Game still going)
    full = IsBoardFull(Board)
    if (Board[1-1][1-1] == 'X') and (Board[1-1][2-1] == 'X') and (Board[1-1][3-1] == 'X'):
        return 1
    elif (Board[1-1][1-1] == 'X') and (Board[2-1][1-1] == 'X') and (Board[3-1][1-1] == 'X'):
        return 1
    elif (Board[1-1][1-1] == 'X') and (Board[2-1][2-1] == 'X') and (Board[3-1][3-1] == 'X'):
        return 1
    elif (Board[2-1][1-1] == 'X') and (Board[2-1][2-1] == 'X') and (Board[2-1][3-1] == 'X'):
        return 1
    elif (Board[3-1][1-1] == 'X') and (Board[3-1][2-1] == 'X') and (Board[3-1][3-1] == 'X'):
        return 1
    elif (Board[1-1][2-1] == 'X') and (Board[2-1][2-1] == 'X') and (Board[3-1][2-1] == 'X'):
        return 1
    elif (Board[1-1][3-1] == 'X') and (Board[2-1][3-1] == 'X') and (Board[3-1][3-1] == 'X'):
        return 1
    elif (Board[3-1][1-1] == 'X') and (Board[2-1][2-1] == 'X') and (Board[1-1][3-1] == 'X'):
        return 1
    elif (Board[1-1][1-1] == 'O') and (Board[1-1][2-1] == 'O') and (Board[1-1][3-1] == 'O'):
        return 2
    elif (Board[1-1][1-1] == 'O') and (Board[2-1][1-1] == 'O') and (Board[3-1][1-1] == 'O'):
        return 2
    elif (Board[1-1][1-1] == 'O') and (Board[2-1][2-1] == 'O') and (Board[3-1][3-1] == 'O'):
        return 2
    elif (Board[2-1][1-1] == 'O') and (Board[2-1][2-1] == 'O') and (Board[2-1][3-1] == 'O'):
        return 2
    elif (Board[3-1][1-1] == 'O') and (Board[3-1][2-1] == 'O') and (Board[3-1][3-1] == 'O'):
        return 2
    elif (Board[1-1][2-1] == 'O') and (Board[2-1][2-1] == 'O') and (Board[3-1][2-1] == 'O'):
        return 2
    elif (Board[1-1][3-1] == 'O') and (Board[2-1][3-1] == 'O') and (Board[3-1][3-1] == 'O'):
        return 2
    elif (Board[3-1][1-1] == 'O') and (Board[2-1][2-1] == 'O') and (Board[1-1][3-1] == 'O'):
        return 2
    elif full == True:
        return 3
    else:
        return 0

    '''
    Parameters:
         Board is the current game board, a 3x3 matrix
    Return: Outcome, an integer
        Outcome is 0 if the game is still in progress
        Outcome is 1 if player X wins
        Outcome is 2 if player O wins
        Outcome is 3 if it is a tie (no winner)
    Description:
        this funtion determines the Outcome of the game
    hint:
        (1) check if anyone wins, i.e., three 'X' or 'O' in
            top row, middle row, bottom row
            lef col, middle col, right col
            two diagonals
        (2) if no one wins, then check if it is a tie
                i.e. if the board is fully occupied, then it is a tie
        (3) otherwise, the game is still in progress
    '''

#%%
def ShowOutcome(Outcome, NameX, NameO):
    print()
    print('X:', NameX)
    print('O:', NameO)
    if Outcome == 1 and NameX == 'Computer':
        print('Computer won!')
    elif Outcome == 1 and NameX != 'Computer':
        print(NameX, 'won!')
    elif Outcome == 2 and NameO == 'Computer':
        print('Computer won!')
    elif Outcome == 2 and NameO != 'Computer':
        print(NameO, 'won!')
    elif Outcome == 3:
        print('It is a tie!')
    elif Outcome == 0:
        print('The game is still in progress')
        print()

    '''
    Parameters:
        Outcome is from Judge
        NameX is the name of PlayerX who goes first at the beginning
        NameO is the name of PlayerO 
    Return: None
    Description:
        print a meassage about the Outcome
        NameX/NameO may be 'human' or 'computer'
    hint: the message could be
        PlayerX (NameX, X) wins 
        PlayerO (NameO, O) wins
        the game is still in progress
        it is a tie
    '''

#%% read but do not modify this function
def Which_Player_goes_first():
    if random.randint(0, 1) == 0:
        print()
        print("Computer player goes first")
        PlayerX = ComputerPlayer        
        PlayerO = HumanPlayer     
    else:
        print()
        print("Human player goes first")
        PlayerO = ComputerPlayer        
        PlayerX = HumanPlayer           
    return PlayerX, PlayerO

    '''
    Parameter: None
    Return: two function objects: PlayerX, PlayerO
    Description:
        Randomly choose which player goes first.  
        PlayerX/PlayerO is ComputerPlayer or HumanPlayer
    '''

#%% the game
def TicTacToeGame():
    #---------------------------------------------------    
    print("Welcome to Tic Tac Toe Game")
    Board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    DrawBoard(Board)
    # determine the order of the players
    PlayerX, PlayerO = Which_Player_goes_first()
    # get the name of each function object
    NameX = PlayerX.__name__
    NameO = PlayerO.__name__
    #---------------------------------------------------    
    # suggested steps in a while loop:
    # (1)  get the choice from PlayerX, e.g. ChoiceX=PlayerX('X', Board)
    # (2)  update the Board
    # (3)  draw the Board
    # (4)  get the outcome from Judge
    # (5)  show the outcome
    # (6)  if the game is completed (win or tie), then break the loop
    # (7)  get the choice from PlayerO
    # (8)  update the Board
    # (9)  draw the Board
    # (10) get the outcome from Judge
    # (11) show the outcome
    # (12) if the game is completed (win or tie), then break the loop
    #---------------------------------------------------

    # your code starts from here
    playerName = input("what is your name?: ")
    gameComplete = 0
    if PlayerX == ComputerPlayer:
        while gameComplete == 0:
            ChoiceX = ComputerPlayer('X', Board)
            UpdateBoard(Board, 'X', ChoiceX)
            DrawBoard(Board)
            outcome = Judge(Board)
            ShowOutcome(outcome, 'Computer', playerName)
            if((outcome == 1) or (outcome == 2) or (outcome == 3)):
                gameComplete = 1
                break
            ChoiceO = HumanPlayer('O', Board)
            UpdateBoard(Board, 'O', ChoiceO)
            DrawBoard(Board)
            outcome = Judge(Board)
            ShowOutcome(outcome, 'Computer', playerName)
            if((outcome == 1) or (outcome == 2) or (outcome == 3)):
                gameComplete = 1
    elif PlayerX == HumanPlayer:
        while gameComplete == 0:
            ChoiceX = HumanPlayer('X', Board)
            UpdateBoard(Board, 'X', ChoiceX)
            DrawBoard(Board)
            outcome = Judge(Board)
            ShowOutcome(outcome, playerName, 'Computer')
            if((outcome == 1) or (outcome == 2) or (outcome == 3)):
                gameComplete = 1
                break
            ChoiceO = ComputerPlayer('O', Board)
            UpdateBoard(Board, 'O', ChoiceO)
            DrawBoard(Board)
            outcome = Judge(Board)
            ShowOutcome(outcome, playerName, 'Computer')
            if((outcome == 1) or (outcome == 2) or (outcome == 3)):
                gameComplete = 1 
    print()
    print('Author of Game:', author())
    
#%% play the game many rounds until the user wants to quit
# read but do not modify this function
def PlayGame():
    while True:
        TicTacToeGame()
        print("Please type yes to play again or no if not")
        if not input().lower().startswith('y'):
            break
    print("GameOver")

#%% do not modify anything below
if __name__ == '__main__':
    PlayGame()
