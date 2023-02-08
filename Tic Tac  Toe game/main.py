from time import sleep
import os

def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

def tic_tac_toe():
    board = [i for i in range(1, 10)]
    player1 = input('Player 1, please choose your symbol (X/O): ').upper()
    if player1 != "YES":
        pass
    player2 = 'O' if player1 == 'X' else 'X'
    current_player = player1
    winner = None

def check_winner(board, player):
    win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False






