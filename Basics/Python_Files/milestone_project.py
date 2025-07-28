"""
1. Create a function to display the tic tac toe board
2. Accept player one input
3. Validate the player one user input
4. Update the game board positions and display board
5. Check if any player won the game
6. Accept player two input
7. validate the player two input
8. Update the gameboard positions and display board
9. Check if any player won the game
10. Keep running the game until any player wins the game
"""

def get_player_one_choice():
    player_one_choice=' '
    while player_one_choice not in ['X', 'O']:
        player_one_choice=input("Player1, please enter you marker choice, either X or O :")
        if player_one_choice not in ['X', 'O']:
            print("Invalid Input! Please choose either X or O")
        else:
            break
    return player_one_choice

def gameon_choice():
    choice=' '
    while choice not in ['Yes', 'No', 'yes', 'no', 'Y', 'N', 'y', 'n']:
        choice=input("Do You want to keep playing, please input Yes or No : ")
        if choice not in ['Yes', 'No', 'yes', 'no', 'Y', 'N', 'y', 'n']:
            print("Invalid Input! Please input either Yes or No")
        else:
            break
    if choice in ['Yes', 'yes', 'Y', 'y']:
        return True
    else:
        return False

def display_board(game_board):
    pipe_delimiter="|"
    line_delimiter="-----"
    tab_padding="\t\t\t\t\t"
    print(f"{tab_padding}{game_board[7]}{pipe_delimiter}{game_board[8]}{pipe_delimiter}{game_board[9]}")    
    print(tab_padding+line_delimiter)
    print(f"{tab_padding}{game_board[4]}{pipe_delimiter}{game_board[5]}{pipe_delimiter}{game_board[6]}")
    print(tab_padding+line_delimiter)
    print(f"{tab_padding}{game_board[1]}{pipe_delimiter}{game_board[2]}{pipe_delimiter}{game_board[3]}")

def clear_board(game_board):
    game_board=[" "]*10
    return game_board

def replace_board_cell(game_board,value,position):
    game_board[position]=value
    return game_board

def get_player_one_input():
    position=''    
    while position.isdigit()==False or int(position) not in range(1,11):
        position=input("Player 1, please pick a position from 1 to 9: ")        
        if position.isdigit()==False:
            print("Invalid input! Please enter a number from 1 to 9")
        if int(position) not in range(1,11):
            print("Invalid input! Please enter a number from 1 to 9")
        else:
            break
    return int(position)

def get_player_two_input():
    position=''    
    while position.isdigit()==False or int(position) not in range(1,11):
        position=input("Player 2, please pick a position from 1 to 9: ")        
        if position.isdigit()==False:
            print("Invalid input! Please enter a number from 1 to 9")
        if int(position) not in range(1,11):
            print("Invalid input! Please enter a number from 1 to 9")
        else:
            break
    return int(position)

def check_board_pos(game_board,position):
    if game_board[int(position)]==' ':
        return True
    else:
        print("The cell is not empty! Please pick a different cell")
        return False

def check_if_board_is_full(game_board):
    for x in range(1,10):
        if game_board[x]==' ':
            return False
    return True

def check_if_player_won(game_board,player_one_choice, player_two_choice):
    winning_combinations=[(7,8,9),(4,5,6),(1,2,3),(7,4,1),(8,5,2),(9,6,3),(7,5,3),(9,5,1)]
    for combo in winning_combinations:
        if game_board[combo[0]]==game_board[combo[1]]==game_board[combo[2]]==player_one_choice:            
            return True
        elif game_board[combo[0]]==game_board[combo[1]]==game_board[combo[2]]==player_two_choice:            
            return True
        else:
            continue
    return False

def set_player_two_choice(player_one_choice):
    if player_one_choice=='X':
        return 'O'
    else:
        return 'X'

def reset_game(game_board):
    display_board(game_board)
    game_board = game_board=[" "]*10
    player_one_choice=' '
    player_two_choice=' '
    return (game_board, player_one_choice, player_two_choice)


def game_run():
    game_on=True
    game_board=[" "]*10
    player_one_position=' '
    player_two_position=' '
    player_one_choice=' '
    player_two_choice=' '
    print("\t\t\tWELCOME TO TIC TAC TOE CONSOLE GAME!")    
    display_board(game_board)
    game_on=gameon_choice()
    while game_on and check_if_board_is_full(game_board)==False:
        if game_on==False:
            break
        if player_one_choice==' ':
            player_one_choice=get_player_one_choice()
        else:
            pass
        if player_two_choice==' ':
            player_two_choice=set_player_two_choice(player_one_choice)
        else:
            pass
        if player_one_choice!=' ':
            player_one_position=get_player_one_input()            
            while check_board_pos(game_board,player_one_position)==False:                
                player_one_position = get_player_one_input()
            else:
                pass
            replace_board_cell(game_board,player_one_choice,player_one_position)
            display_board(game_board)
            if check_if_player_won(game_board,player_one_choice,player_two_choice)==True:
                print("Player 1, has won the game!")            
                game_board,player_one_choice,player_two_choice=reset_game(game_board)               
                game_on=gameon_choice()
            else:
                pass
            if check_if_board_is_full(game_board)==True:
                print("The game is a draw!")
                game_board,player_one_choice,player_two_choice=reset_game(game_board)
                game_on=gameon_choice()
            else:
                pass
        else:
            pass  
        if player_two_choice!=' ':
            player_two_position=get_player_two_input()            
            while check_board_pos(game_board,player_two_position)==False:                
                player_two_position = get_player_two_input()
            else:
                pass
            replace_board_cell(game_board,player_two_choice,player_two_position)
            display_board(game_board)
            if check_if_player_won(game_board,player_two_choice,player_two_choice)==True:
                print("Player 2, has won the game!")            
                game_board,player_one_choice,player_two_choice=reset_game(game_board)                 
                game_on=gameon_choice()
            else:
                pass
            if check_if_board_is_full(game_board)==True:
                print("The game is a draw!")
                game_board,player_one_choice,player_two_choice=reset_game(game_board)
                game_on=gameon_choice()
            else:
                pass
        else:
            pass
    else:
        print("Game Over!")

game_run()