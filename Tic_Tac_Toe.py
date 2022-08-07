# OBJECTIVE
'''
Make a tic tac toe game through terminal.
'''

# IMPORTS
import os
import time

# VARIABLES
game_list = ['placeholder', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# FUNCTIONS
def intro_message():
	'''
	Display the introduction message to the players along with the board design.
	The system('clear') command is for Mac NOT Windows.
	'''
	print("Welcome to Tic Tac Toe!\n")
	print('''The rules are simple. You will choose to be Player 1 ("X") or Player 2 ("O"). The board is designed in the format seen below. In order to play you will provide the number slot to the system where you want to add your "X" or "O". The first one to get three in a row, column, or diagonal wins!\n\nGood luck!\n
		''')
	print('1 | 2 | 3')
	print("---------")
	print('4 | 5 | 6')
	print("---------")
	print('7 | 8 | 9')
	print('\n')
	time.sleep(15)
	os.system('clear')

def display_game(board):
	'''
	Show the "board" on the terminal.
	'''
	print("Current board:\n")
	print(board[1] + ' | ' + board[2] + ' | ' + board[3])
	print("---------")
	print(board[4] + ' | ' + board[5] + ' | ' + board[6])
	print("---------")
	print(board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('\n')

def player_selection():
	'''
	Ask for Player 1 to choose between X or O then assign Player 2 as the opposite.
	Output is Tuple
	'''
	selection = ''
	while selection != 'X' and selection != 'O':
		selection = input("Player 1, do you want to be X or O ('X' or 'O')? ")
	player1 = selection
	if player1 == 'X':
		player2 = 'O'
	else:
		player2 = 'X'
	return(player1,player2)

def is_win(my_list):
	# Variables
	x_win = ['X','X','X']
	o_win = ['O','O','O']
	first_col = my_list[1::3]
	second_col = my_list[2::3]
	third_col = my_list[3::3]
	diagonal_one = my_list[1::4]
	diagonal_two = my_list[3:8:2]
	x_won = False
	o_won = False
	who_wins = ''

	# Check X against rows, columns, and diagonals to see if victorious
	if (my_list[1:4] == x_win) or (my_list[4:7] == x_win) or (my_list[7:] == x_win):
		x_won = True
	elif (first_col == x_win) or (second_col == x_win) or (third_col == x_win):
		x_won = True
	elif (diagonal_one == x_win) or (diagonal_two == x_win):
		x_won = True

	# Check Y against rows, columns, and diagonals to see if victorious	
	if (my_list[1:4] == o_win) or (my_list[4:7] == o_win) or (my_list[7:] == o_win):
		o_won = True
	elif (first_col == o_win) or (second_col == o_win) or (third_col == o_win):
		o_won = True
	elif (diagonal_one == o_win) or (diagonal_two == o_win):
		o_won = True

	if x_won:
		who_wins = 'X'
		return who_wins
	elif o_won:
		who_wins = 'O'
		return who_wins
	else:
		who_wins = 'no winner'
		return who_wins

def user_choice(players, winner, tic_tac_toe_list):
	while (winner != 'X') and (winner != 'O'):
		if ' ' not in tic_tac_toe_list:
			print("Stalemate! Game Over!")
			break
		first_player = input("X, what is your selection (1 - 9)? ")
		while input_check(first_player,tic_tac_toe_list) == False:
			first_player = input("X, what is your selection (1 - 9)? ")
		
		tic_tac_toe_list[input_check(first_player,tic_tac_toe_list)] = 'X'
		os.system('clear')
		display_game(tic_tac_toe_list)
		winner = is_win(tic_tac_toe_list)
		if winner == 'X' and players[0] == 'X':
			print("Player 1 has won! Congratulations!")
			break
		elif winner == 'X' and players[1] == 'X':
			print("Player 2 has won! Congratulations!")
			break
		
		if ' ' not in tic_tac_toe_list:
			print("Stalemate! Game Over!")
			break
		second_player = input("O, what is your selection (1 - 9)? ")
		while input_check(second_player,tic_tac_toe_list) == False:
			second_player = input("O, what is your selection (1 - 9)? ")

		tic_tac_toe_list[input_check(second_player,tic_tac_toe_list)] = 'O'	
		os.system('clear')
		display_game(tic_tac_toe_list)
		winner = is_win(tic_tac_toe_list)
		if winner == 'O' and players[0] == 'O':
			print("Player 1 has won! Congratulations")
			break
		elif winner == 'O' and players[1] == 'O':
			print("Player 2 has won! Congratulations")
			break

def input_check(test_input,board_list):
	passed_test = True
	if test_input.isdigit():
		input_to_int = int(test_input)
		if input_to_int in [1,2,3,4,5,6,7,8,9]:
			if board_list[input_to_int] == ' ':
				return input_to_int
			else:
				print("Pay attention, dipshit! That number was played!")
				passed_test = False
				return passed_test
		else:
			print("Acceptable range is 1 - 9, blind fuck!")
			passed_test = False
			return passed_test
	else:
		print("Provide a number, dumb fuck!")
		passed_test = False
		return passed_test

# SCRIPT
intro_message()
display_game(game_list)
player_tuple = player_selection()

if player_tuple[0] == 'X':
	print("Player 1 is " + player_tuple[0] + " and goes first!")
	print("Player 2 is " + player_tuple[1] + " and goes second!")
else:
	print("Player 2 is " + player_tuple[1] + " and goes first!")
	print("Player 1 is " + player_tuple[0] + " and goes second!")

default_try = is_win(game_list)

user_choice(player_tuple, default_try, game_list)