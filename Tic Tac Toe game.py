import random

# Creating some global variables
winner = None
Game_running = True
current_player = "X"

board = ['=', '=', '=',
         '=', '=', '=',
         '=', '=', '=']


# Creating a game board
def gamestructure(board):
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('---------')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('---------')
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('---------')


# Taking input of the X or O
def input_maker(board):
    global current_player
    while True:
        try:
            integer = int(input(f"Player {current_player}, enter a number from 1 to 9: ")) - 1
            if integer >= 0 and integer <= 8 and board[integer] == "=":
                board[integer] = current_player
                break
            else:
                print('Invalid Input, try again.')
        except ValueError:
            print('Please enter a valid integer.')


# Applying Conditions
# Horizontal condition
def condition1(board):
    global winner
    if board[8] == board[7] == board[6] and board[8] != '=':
        winner = board[8]
        return True
    elif board[5] == board[4] == board[3] and board[5] != '=':
        winner = board[5]
        return True
    elif board[2] == board[1] == board[0] and board[2] != '=':
        winner = board[2]
        return True
    return False

# Column Conditions
def condition2(board):
    global winner
    if board[8] == board[5] == board[2] and board[2] != '=':
        winner = board[8]
        return True
    elif board[7] == board[4] == board[1] and board[7] != '=':
        winner = board[7]
        return True
    elif board[6] == board[3] == board[0] and board[6] != '=':
        winner = board[6]
        return True
    return False

# Angle Conditions
def condition3(board):
    global winner
    if board[8] == board[4] == board[0] and board[8] != '=':
        winner = board[8]
        return True
    elif board[2] == board[4] == board[6] and board[2] != '=':
        winner = board[2]
        return True
    return False

# Checking Winner
def Jurdge():
    global Game_running
    if condition3(board) or condition2(board) or condition1(board):
        print(f"The winner is {winner}")
        Game_running = False

# Tie checker
def game_tie(board):
    global Game_running
    if "=" not in board:
        print("It's a tie!")
        Game_running = False

# Switching player function
def switching_moving_power():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    
    #computer bot giving a input
def computer(board):
	
	
	while current_player=="O":
		random_integer=random.randint(1,9)
		
		if board[random_integer-1]=="=":
		   board[random_integer-1]=current_player
		   	
		   print(f"Computr chose {random_integer}")
		   break
		   
		
		

# Running all codes
while Game_running:
	gamestructure(board)
	
	
	switching_moving_power()
	if current_player =="X":
		input_maker(board)
	else:
		computer(board)
		
	Jurdge()
	game_tie(board)
