def board_print(board):
    print("Welcome to Tic Tac Toe Game")
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("-----")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("-----")
    print(board[6]+"|"+board[7]+"|"+board[8])

def player_input():
    
    playerone = ''
    playertwo = ''
    while playerone != 'X' and playerone != 'O':
        playerone = input("Player 1, please choose you symbol: ")
    
    if playerone == 'X':
        playertwo = 'O'
    else:
        playertwo = 'X'
    
    return (playerone, playertwo)

def update_board():
    pass

def check_game():
    pass

def ask_players():
    pass

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
player1 = ''
player2= ''

board_print(board)
result = player_input()
print(result)