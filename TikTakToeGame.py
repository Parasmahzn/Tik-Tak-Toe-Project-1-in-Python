# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 05:52:36 2019

@author: paras
"""

import random

def display_board(board):
    print('\n')
    print('\n'*100)
    print('\t '+board[7]+'  |'+' '+board[8]+'  '+'| '+ board[9])
    print('\t----|----|---')
    print('\t '+ board[4]+'  |'+' '+board[5]+'  '+'| '+ board[6])
    print('\t----|----|---')
    print('\t '+ board[1]+'  |'+' '+board[2]+'  '+'| '+ board[3])              

#test_board=['#','X','O','X','O','X','O','X','O','X']



# Taking player input and assigning their markers            
def player_input():
    
        marker=''
        #Keep asking player one to choose X or O
        while marker !='X' and marker !='O':
            marker=input("PLAYER 1:  Choose X or O: ")
        #Choosing alternate marker for Player 2
        if marker =='X':
            return ('X','O')
        else:
            return ('O','X')
        

#Placing markers on the board
def place_marker(board,marker,position):
    board[position]=marker
 

#Check to see if given marks win    
def win_check(board,mark):
        
    # Checking each winning possibles
    if(mark==board[1] and mark==board[2] and mark==board[3]):
        #print(f'{mark} ::: 1 {board[1]} 2 {board[2]} 3 {board[3]}')
        return True
    elif(mark==board[4] and mark==board[5] and mark==board[6]):
        #print(f'{mark} ::: 4 {board[4]} 5 {board[5]} 6 {board[6]}')
        return True        
    elif(mark==board[7] and mark==board[8] and mark==board[9]):
        #print(f'{mark} ::: 7 {board[7]} 8 {board[8]} 9 {board[9]}')
        return True        
    elif(mark==board[1] and mark==board[4] and mark==board[7]):
        #print(f'{mark} ::: 1 {board[1]} 4 {board[4]} 7 {board[7]}')
        return True
    elif(mark==board[2] and mark==board[5] and mark==board[8]):
        #print(f'{mark} ::: 2 {board[2]} 5 {board[5]} 8 {board[8]}')
        return True
    elif(mark==board[3] and mark==board[6] and mark==board[9]):
        #print(f'{mark} ::: 3 {board[3]} 6 {board[6]} 9 {board[9]}')
        return True
    elif(mark==board[1] and mark==board[5] and mark==board[9]):
       #print(f'{mark} ::: 1 {board[1]} 5 {board[5]} 9 {board[9]}')
        return True
    elif(mark==board[4] and mark==board[5] and mark==board[6]):
        #print(f'{mark} ::: 4 {board[4]} 5 {board[5]} 6 {board[6]}')
        return True
    elif(mark==board[3] and mark==board[5] and mark==board[7]):
        #print(f'{mark} ::: 3 {board[3]} 5 {board[5]} 7 {board[7]}')
        return True
    else:
        return False


#Choose random player who goes first
def choose_first():
    start_player = random.randint(1,2)
    if(start_player==1):
        return "Player 1" 
    else:
        return "Player 2"
    
#Checking whether a space on the board is available to put a mark on    
def space_check(board,position):
    return board[position]==' '


#Cheking if the board is full or not?
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True # Board is full
    

#Asking for players next positions (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a Position: [1-9] '))
    return position

#Asking to continue playing
def replay():
    replay=input("Do you want to continue playing? [Yes(Y)/No(N)] :")
    if(replay.upper()=='Y' or replay.upper()=='YES'):
        return True
    elif(replay.upper()=='N' or replay.upper()=='NO'):
        return False
    else:
        pass
    

#Main Execution of Tik Tac Toe
print('\n\n\nWELCOME to TIC TAC TOE!\n')

while True:
    
    #Play the Game
    #Setup the game play(Board,Player1,Player2,Markers,0,X)
    the_board=['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
    player1_marker,player2_marker=player_input()
    
    turn=choose_first()
    print('\n'+turn+" will go first!")
    
    play_game=input('Ready to Play? (y/n) : ')
    if play_game=='y':
        game_on=True
    else:
        game_on=False
        
        #Game Play
        
    while game_on:
        if turn=='Player 1':
         ##Player 1        
             display_board(the_board)
             print('Player 1 :')
             position= player_choice(the_board)
             place_marker(the_board,player1_marker,position)
             if win_check(the_board,player1_marker):
                 display_board(the_board)
                 print('\nCongratulations!! Player 1 has Won the Game')
                 game_on=False
             else:
                 if full_board_check(the_board):
                     display_board(the_board)
                     print("\nOpps!! There's a tie")
                     game_on=False
                 else:
                     turn='Player 2'
        else:
             display_board(the_board)
             print('Player 2 :')
             position= player_choice(the_board)
             place_marker(the_board,player2_marker,position)
             if (win_check(the_board,player2_marker)):
                 display_board(the_board)
                 print('\nCongratulations!! Player 2 has Won the Game')
                 game_on=False
             else:
                 if(full_board_check(the_board)):
                     display_board(the_board)
                     print("\nOpps!! There's a tie")
                     game_on=False
                 else:
                     turn='Player 1'
            
    if not replay():
        break
# End the game if users don't wanna continue