import numpy as np
import pygame
import sys
import math

ROW = 3 
COL = 3

CROSS_COLOUR =(66,66,66)
BLUE = (28,170,156)
BLACK = (0,0,0)
WHITE = (239,231,200)
LINE_COL = (23,145,135)

WIDTH =600
HEIGHT =600
LINE_WIDTH = 15
CIRCLE_RAD =60
CIRCLE_WIDTH = 15

SPACE = 55
CROSS_WIDTH = 20
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BLUE)


pygame.display.update()

#creating board     #optimize

def create_board():
    board = np.zeros((ROW,COL))
    return board

def is_valid_location(board,r,c):
    return board[r][c] == 0

def p_input(board,r,c,piece):
     board[r][c] = piece




def draw_check(board):
    if 0 in board:
        return False
    else:
        return True
    
def  vertical_win_line(c,piece):
    col = c * 200 + 100
    
    if piece == 1:
        color = WHITE
    elif piece == 2:
        color = CROSS_COLOUR
        
    pygame.draw.line(screen, color, (col,15), (col, HEIGHT-15), 15)    
    
def horizontal_win_line(r,piece):
    row = r * 200 + 100
    
    if piece == 1:
        color = WHITE
    elif piece == 2:
        color = CROSS_COLOUR
        
    pygame.draw.line(screen, color, (15,row), (WIDTH-15 , row), 15)    
    
def negative_diag_win(piece):
    
    if piece == 1:
        color = WHITE
    elif piece == 2:
        color = CROSS_COLOUR
    
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH-15 , 15), 15)
    
    
def positive_diag_win(piece):
    
    if piece == 1:
        color = WHITE
    elif piece == 2:
        color = CROSS_COLOUR
    
    pygame.draw.line(screen, color, (15,15), (WIDTH - 15, HEIGHT-15), 15)
    
    
def winner(board,r,c,piece):
    #vertical 
    output = False
    
    if board[0][c] == piece and board[1][c] == piece and board[2][c] == piece: # vertical win
        vertical_win_line(c,piece)
        output = True
        
    elif board[r][0] == piece and board[r][1] == piece and board[r][2] == piece: #horizontal win   
        horizontal_win_line(r,piece)
        output = True
            
    elif board[0][0] == piece and board[1][1] == piece and board[2][2] == piece: # positive slope win 
        positive_diag_win(piece)
        output = True    
                 
              
    elif  board[2][0] == piece and board[1][1] == piece and board[0][2] == piece: # negative slope win
        negative_diag_win(piece) 
        output = True

    return output    

def draw_figs(board, r,c):
    # for row in range(ROW):
    #     for col in range(COL):
            if board[r][c] == 1:
                pygame.draw.circle( screen , WHITE, (int(c * 200 + 100 ), int( r * 200 + 100)) , CIRCLE_RAD, CIRCLE_WIDTH )
                
            else:
                pygame.draw.line( screen , CROSS_COLOUR  , (c * 200 + SPACE , r * 200 + 200 - SPACE) , (c * 200 +200 - SPACE, r * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line( screen , CROSS_COLOUR  , (c * 200 + SPACE , r * 200 + SPACE) , (c * 200 + 200 - SPACE, r * 200 + 200 - SPACE), CROSS_WIDTH)
            pygame.display.update()
                
                
                            
def draw_lines():
    pygame.draw.line( screen , LINE_COL, (0,200), (600,200), LINE_WIDTH)
    pygame.draw.line( screen , LINE_COL, (0,400), (600,400), LINE_WIDTH)
    pygame.draw.line( screen , LINE_COL, (200,0), (200,600), LINE_WIDTH)
    pygame.draw.line( screen , LINE_COL, (400,0), (400,600), LINE_WIDTH)
    
    
draw_lines()
    
pygame.display.update()
    
board = create_board()
print(board)
turn = 0
game_over = False


while not game_over:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
         
        if event.type == pygame.MOUSEBUTTONDOWN:
           # print(event.pos)
            #player 1 turn 
           
            
            if turn == 0:
                c = int(math.floor(event.pos[0])//200)
                r = int(math.floor(event.pos[1])//200)
                #print(r,c)
                
               # r = int(input("player 1: "))
                #c = int(input("player 1 again: "))
                
                if is_valid_location(board,r,c):
                    p_input(board,r,c,1)
                    draw_figs(board,r,c)
                else:
                    print("Already filled, Please try again")
                    turn = -1
                
                if winner(board,r,c,1) == True :
                    print("YOU WON PLAYER 1 !!")
                    print(board)
                    game_over = True
                    break
                
                
                    
                
            else:
                c = int(math.floor(event.pos[0])//200)
                r = int(math.floor(event.pos[1])//200)
                #print(r,c)
                
                if is_valid_location(board,r,c):
                    p_input(board,r,c,2)
                    draw_figs(board,r,c)
                    
                else:
                    print("Already filled, Please try again")
                    turn = 2    
                    
                
                if winner(board,r,c,2) == True :
                    print("YOU WON PLAYER 2 !!")
                    print(board)
                    game_over = True
                    break
            
            print(board)    
           
            turn +=1
            turn = turn%2
            
            if draw_check(board):
                print("IT'S A DRAW !! PLEASE DO A REMATCH")
                pygame.time.wait(2000)
                game_over = True
                break
                
if  game_over:
    pygame.display.update()
    pygame.time.wait(5000)