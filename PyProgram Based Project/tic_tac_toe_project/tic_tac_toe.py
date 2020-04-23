from random import randint 

def display_board(board):
    
    print('\n'*100)
    print(board[1]+" |"+board[2]+" | "+board[3])
    print("__|__|__ ")
    print(board[4]+" |"+board[5]+" | "+board[6])
    print("__|__|__ ")
    print(board[7]+" |"+board[8]+" | "+board[9])

def player_input():
    
    mark = input("Player1: Do you want to be 'X' or 'O'")
    turn=choose_first()
    print(f'Player{turn} will be first to go on')
    kick=input("Are you ready to play? Enter Yes or No")
    if kick=="Yes":
        pass
    elif kick=="No":
        return
    else:
        print("Enter a valid string!!!!!")

    return mark,turn

def win_check(board, mark):
    
    return  ((board[1]==mark and board[2]==mark and board[3]==mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark))

def choose_first():
    return randint(1,2)

def place_marker(board, marker, position):
    
    board[position]=marker
    display_board(board)

def space_check(board, position):
    
    return board[position]==" "

def full_board_check(board):
    
    return ' ' in board

def replay():
    
    resp=input("Do you want to play again? enter 'Y' for Yes or 'N' for No:")
    return (resp=='Y' or resp=='y')


if __name__ == "__main__":

    print('Welcome to Tic Tac Toe!')
    game_on=True

    while True:
        Mark,Turn=player_input()
        test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        display_board(test_board)
         
        while game_on:
            if (Mark=='X' and Turn==1) or (Mark=='O' and Turn==2):
                while full_board_check(test_board):
                    
                    position = int(input('choose your next position from(1-9)'))
                    if space_check(test_board, position):
                        place_marker(test_board,'X',position)
                    else:
                        print("input 'X' in blank position")
                        continue
                    #display_board(test_board)
                    if win_check(test_board,'X'):
                        print("Hurray! You Won...")
                        break
                    else:
                        pass

                    position = int(input('choose your next position from(1-9)'))
                    if space_check(test_board,position):
                        place_marker(test_board,'O',position)
                    else:
                        print("input 'O' in blank position")
                        continue
                    #display_board(test_board)
                    if win_check(test_board,'O'):
                        print("Hurray! You Won...")
                        break
                    else:
                        pass
                    
                break
                
            else:
                while full_board_check(test_board):
                    
                    position = int(input('choose your next position from(1-9)'))
                    if space_check(test_board, position):
                        place_marker(test_board,'O',position)
                    else:
                        print("input 'O' in blank position")
                        continue
                    #display_board(test_board)
                    if win_check(test_board,'O'):
                        print("Hurray! You Won...")
                        break
                    else:
                        pass
    #                 time.sleep(5)
    #                 clear_output()

                    position = int(input('choose your next position from(1-9)'))
                    if space_check(test_board,position):
                        place_marker(test_board,'X',position)
                    else:
                        print("input 'X' in blank position")
                        continue
                    #display_board(test_board)
                    if win_check(test_board,'X'):
                        print("Hurray! You Won...")
                        break
                    else:
                        pass
    #                 clear_output()
    #                 time.sleep(5)
                break
                    
        if not replay():
            break