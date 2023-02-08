import os


def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---|---|---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---|---|---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')
    

def check_winner(board, player):
    win_conditions = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def tic_tac_toe():
    board = [i for i in range(1, 10)]
    player1 = input('Player 1, please choose your symbol (X/O): ').upper()
    player2 = 'O' if player1 == 'X' else 'X'
    current_player = player1
    winner = None
    

    while True:
        display_board(board)

        move = int(input(f'{current_player}, please choose your next move (1-9): '))

        if board[move - 1] == 'X' or board[move - 1] == 'O':
            print("This cell is already occupied, please choose another one!")
            continue

        board[move - 1] = current_player
        if check_winner(board, current_player):
            winner = current_player
            break

        if not 'X' in board and not 'O' in board:
            winner = 'DRAW'
            break

        current_player = player2 if current_player == player1 else player1

    display_board(board)
    if winner == 'DRAW':
        print("It's a Draw!")
    else:
        print(f'{winner} wins!')


tic_tac_toe()
