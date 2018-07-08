board=[]
#construction of board
def print_board(board_in):
  for i in range(0,len(board_in)):
    print '  '.join(board_in[i])
#---------------------------------------------------------------------------
def check_game(testtuple):
      if testtuple == compselect[0] or testtuple == compselect[1]:
         wow= board[testtuple[0]-1]
         wow[testtuple[1]-1]= '1'
         shipsize +=1
         #print(shipsize1)
         #print_board(board)
      else:
         wow= board[testtuple[0]-1]
         wow[testtuple[1]-1]= 'X'
      return board  
    #print('game over ship destroyed in '+ str(chances1))


#---------------------------------------------------------------------------

bsize= input('enter board size ')
b_size= int(bsize)
for i in range(0, b_size):
   board.append(['O'] * b_size)
print_board(board)

#computer selects 1 battleship locations for 2 players
import random
x1= random.randint(1,b_size)
y1= random.randint(1,b_size)
#x3= random.randint(1,b_size)
#y3= random.randint(1,b_size)
list=[1,-1]

while (True):
  p= random.randint(1,2)
  if p==1:
    x2=x1+random.choice(list)
    y2=y1
  if p==2:
    y2=y1+random.choice(list)
    x2=x1
  if (x2 in range(1,b_size+1) and y2 in range(1,b_size+1)):
    break

#while (True):
  #p= random.randint(1,2)
  #if p==1:
    #x4=x3+random.choice(list)
    #y4=y3
  #if p==2:
    #y4=y3+random.choice(list)
    #x4=x3
  #if (x4 in range(1,b_size+1) and y4 in range(1,b_size+1)):
    #break
compselect= [(x1,y1),(x2,y2)]
#compselect2=[(x3,y3),(x4,y4)]
print(compselect)
#print(compselect2)
#---------------------------------------------------------------------------
#try:
print('GAME ON') 

shipsize=0
chances1=0
chances2=0
while shipsize != 2:
  print('user 1 and user2 Enter Position of attack')
  a1 = raw_input()
  a2 = raw_input()
  testtuple1= tuple(map(int,a1.split(',')))
  chances1 += 1
  testtuple2= tuple(map(int,a2.split(',')))
  chances2 += 1
  check_game(testtuple1)
  check_game(testtuple2)

  #print('game for user2')
  #print_board(board2)
  #shipsize2=0
  #chances2=0
  #while shipsize2 != 2:
    #print("Enter Position of attack")
    #a2= raw_input()
    #testtuple2= tuple(map(int,a2.split(',')))
    #chances2 +=1
    #if testtuple2 == compselect2[0] or testtuple2 == compselect2[1]:
       #wow2= board2[testtuple2[0]-1]
       #wow2[testtuple2[1]-1]= '1'
       #shipsize2 += 1
       #print(shipsize)
       #print_board(board2)
    #else:
       #wow2= board2[testtuple2[0]-1]
       #wow2[testtuple2[1]-1]= 'X'
       #print_board(board2)
  #print('game over ship destroyed in '+ str(chances2))

if (chances1==chances2):
   print('players tie')
elif (chances1>chances2):
   print('player 2 wins')
else:
   print('player1 wins')

#except: 
   #print('please enter input within the range')
     

----------------------------------------------------------------


while ship size !2
chance=+1

take user input (x,y)

if (x,y) is eqaul to (x1,y1) or (x2,y2)
   print grid with (x,y)=1
   shipsize=+1
   update y at board[x] with 1
   
else
   print grid with (x,y)= *
   update y at board[x] with *
      
 0 0 0 0 0
 0 0 0 0 0
 0 s s 0 0
 0 0 0 0 0
 0 0 0 0 0
 
 x 0 0 0 0
 0 0 0 0 0
 0 s s 0 0
 0 0 0 0 0
 0 0 0 0 0
 
 x x 0 0 0
 0 0 0 0 0
 0 s s 0 0
 0 0 0 0 0
 0 0 0 0 0
 
 x x x 0 0
 0 0 0 0 0
 0 s s 0 0
 0 0 0 0 0
 0 0 0 0 0
 
 
 board = []
for i in range(1,6):
  board.append(['O'] * 5)
  print (board)
def print_board(board_in):
  for i in range(0,len(board_in)):
    print ''.join(board_in[i])
    
  
print_board(board)

---------------------------------------------------------------
---------------------------------------------------------------
import random

shipsize=0
chances1=0
chances2=0


#construction of board
def print_board(board_in):
  for i in range(0,len(board_in)):
    print '  '.join(board_in[i])
#-------------------------------
def check_game(testtuple):
      global shipsize
      board1= board[:]
      if testtuple == compselect[0] or testtuple == compselect[1]:
         wow= board1[testtuple[0]-1]
         wow[testtuple[1]-1]= '1'
         shipsize +=1
         #print(shipsize1)
         print_board(board1)
      else:
         wow= board1[testtuple[0]-1]
         wow[testtuple[1]-1]= 'X'
      	 print_board(board1)	 
    #print('game over ship destroyed in '+ str(chances1))
#-------------------------------
board = []
bsize= input('enter board size ')
b_size= int(bsize)
for i in range(0, b_size):
   board.append(['O'] * b_size)
print_board(board)
#-------------------------------

x1= random.randint(1,b_size)
y1= random.randint(1,b_size)
#x3= random.randint(1,b_size)
#y3= random.randint(1,b_size)
list=[1,-1]

while (True):
  p= random.randint(1,2)
  if p==1:
    x2=x1+random.choice(list)
    y2=y1
  if p==2:
    y2=y1+random.choice(list)
    x2=x1
  if (x2 in range(1,b_size+1) and y2 in range(1,b_size+1)):
    break
compselect= [(x1,y1),(x2,y2)]
print(compselect)
#-------------------------------
print(shipsize)
while shipsize != 2:
  print('user 1 and user2 Enter Position of attack')
  a1 = raw_input()
  a2 = raw_input()
  testtuple1= tuple(map(int,a1.split(',')))
  chances1 += 1
  testtuple2= tuple(map(int,a2.split(',')))
  chances2 += 1
  check_game(testtuple1)
  check_game(testtuple2)
----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
