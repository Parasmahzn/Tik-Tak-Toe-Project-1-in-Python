# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 05:52:36 2019

@author: paras
"""

import random

def display_board(board):
    
        print('\n')
#        print('\n'*100)
        print('\t '+board[7]+' | '+board[8]+' | '+ board[9])
        print('\t---|---|----')
        print('\t '+ board[4]+' | '+board[5]+' | '+ board[6])
        print('\t---|---|----')
        print('\t '+ board[1]+' | '+board[2]+' | '+ board[3])
              

#test_board=['#','X','O','X','O','X','O','X','O','X']



# Taking player input and assigning their markers            
def player_input():
    
        marker=''
        #Keep asking player one to choose X or O
        while marker !='X' and marker !='O':
            marker=input("Player 1, Choose X or O: ")
        #Choosing alternate marker for Player 2
        if marker =='X':
            return {'P1': 'X','P2':'O'}
        else:
            return {'P1':'O','P2':'X'}

#Placing markers on the board
def place_marker(board,marker,position):
    if(position==1):
        board[1]=marker
    elif(position==2):
        board[2]=marker
    elif(position==3):
        board[3]=marker
    elif(position==4):
        board[4]=marker
    elif(position==5):
        board[5]=marker
    elif(position==6):
        board[6]=marker
    elif(position==7):
        board[7]=marker
    elif(position==8):
        board[8]=marker
    else:
        board[9]=marker
 
    display_board(board)
   

#Check to see if given marks win    
def win_check(board,mark):
    print (mark)
    
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
    return (board[position]=="")


#Cheking if the board is full or not?
def full_board_check(board):
    return (len(board)==10)
    

#Asking for players next positions (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.
def player_choice(board):
    choice=0
    while choice >10 and choice<=0:
        choice= int(input('Enter your next position:[1-9]  ' ))
    if(space_check(board,choice)):
        return choice

#Asking to continue playing
def replay():
    replay=input("Do you want to continue playing? [Yes(Y)/No(N)] :")
    if(replay.upper()=='Y' or replay.upper()=='YES'):
        return True
    elif(replay.upper()=='N' or replay.upper()=='NO'):
        return False
    else:
        pass
    
