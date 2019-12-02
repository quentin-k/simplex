import random as rand
import os

board = [[2,2,2,2],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1]]
row =['','','','']

def print_piece(piece):
   if piece == 0:
      return ' '
   elif piece == 2:
      return 'X'
   else:
      return 'O'

def disp_board():
   os.system("clear")
   print('   1 2 3 4   ')
   print('  ┌─┬─┬─┬─┐  ')
   for i in range(len(board)):
      for j in range(len(board[i])):
         row[j] = print_piece(board[i][j])
      print(str(i+1)+ ' │'+row[0]+'│'+row[1]+'│'+row[2]+'│'+row[3]+'│ '+str(i+1))
      if i != len(board) - 1:
         print('  ├─┼─┼─┼─┤  ')
      else:
         print('  └─┴─┴─┴─┘  ')
         print('   1 2 3 4   ')

def get_coords():
   while True:
      try:
         #gets coords
         coord1 = int(input("Type the row and column of the piece you wish to move ie 64: "))
         coord2 = int(input("Type the row and column of where you wish to move your piece: "))
         okay = True
      except ValueError:
         print("Invalid Input!")
         okay = False
      if okay:
         return [int(coord1/10)-1, coord1%10-1, int(coord2/10)-1, coord2%10-1]

def check_placing(player):
   num = 0
   for i in range(6):
      for j in range(4):
         if board[i][j] == player:
            num += 1
   if num == 4:
      return False
   else:
      return True

def check_coords(coords, player, placing):
   
   #makes sures coordinates are in the board
   if coords[0] >= 0 and coords[0] <= 5:
      if coords[1] >= 0 and coords[1] <= 3:
         if coords[2] >= 0 and coords[2] <= 5:
            if coords[3] >= 0 and coords[3] <= 3:
               pass
            else:
               print("Invalid coordinate!")
               return False
         else:
            print("Invalid coordinate!")
            return False
      else:
         print("Invalid coordinate!")
         return False
   else:
      print("Invalid coordinate!")
      return False
   
   #basic checks
   if board[coords[0]][coords[1]] != player and not placing:
      print("That's not you!")
      return False
   if board[coords[2]][coords[3]] != 0 and placing:
      print("That spot is taken!")
      return False
   
   #intermediate checks
   if placing:
      if player == 1:
         able_test = 0
         for i in range(4):
            if board[5][i] == 0:
               able_test += 1
         if able_test > 0:
            able = True
         else:
            able = False

         if coords[0] != 5 and coords[0] != coords[2] and coords[1] != coords[3] and able:
            print("Invalid placement!")
            return False
         elif coords[0] == 5 and coords[0] == coords[2] and coords[1] == coords[3] and able:
            return True
         elif coords[0] != 5:
            print("Invalid choice!")
         elif board[i][j] != player:
            print("Invalid choice!")
            return False
      else:
         able_test = 0
         for i in range(4):
            if board[0][i] == 0:
               able_test += 1
         if able_test > 0:
            able = True
         else:
            able = False

         if coords[0] != 0 and coords[0] != coords[2] and coords[1] != coords[3] and able:
            print("Invalid placement!")
            return False
         elif coords[0] == 0 and coords[0] == coords[2] and coords[1] == coords[3] and able:
            return True
         elif coords[0] != 0:
            print("Invalid choice!")
         elif board[i][j] != player:
            print("Invalid choice!")
            return False

   #advanced checks
   
   #y value check
   if player == 1:
      c1 = coords[0] - coords[2]
   else:
      c1 = coords[2] - coords[0]
   
   #x value check
   c2 = abs(coords[1] - coords[3])

   if c1 == 1 or c1 == 2:
      if c2 == 0 or c2 == c1:
         if c1 == 1:
            return True
         else:
            c3 = [0,0]

            #sets the first coord
            if player == 1:
               c3[0] = coords[2] + 1
            else:
               c3[0] = coords[0] + 1
            
            #sets the second coord
            if coords[1] == coords[3]:
               c3[1] = coords[1]
            elif coords[1] > coords[3]:
               c3[1] = coords[3] + 1
            else:
               c3[1] = coords[1] + 1
            
            #checks fpr valid jump
            c4 = board[c3[0]][c3[1]] #c4 gets the board piece
            if c4 != player and c4 != 0:
               return 1
            else:
               print("Invalid jump!")
               return False
      else:
         print("That spot is too far away!")
         return False
   else:
      print("That spot is too far away!")
      return False

def move_piece(coords, player, jump):
   
   if jump:
      jcoords = [0,0]
      
      #get first jcoords
      if coords[0] > coords[2]:
         jcoords[0] = coords[2] + 1
      else:
         jcoords[0] = coords[0] + 1
      
      #get second jcoords
      if coords[1] == coords[3]:
         jcoords[1] = coords[1]
      elif coords[1] > coords[3]:
         jcoords[1] = coords[3] + 1
      else:
         jcoords[1] = coords[1] + 1
      
      #sets the board
      board[jcoords[0]][jcoords[1]] = 0
   
   #sets the board
   board[coords[0]][coords[1]] = 0
   board[coords[2]][coords[3]] = player

def place_piece(coords, player):
   board[coords[0]][coords[1]] = player

def game():
   player = 0
   running = True
   placing = False
   while running:
      #show board
      print(' ')
      disp_board()
      print(' ')

      #set player
      player += 1
      player %= 2
      player = 2 - player

      #get coords
      fail = True
      jump = False
      while fail:
         print("It is player "+ str(player) + "'s turn")
         coords = get_coords()
         placing = check_placing(player)
         check = check_coords(coords, player, placing)
         if check == 1:
            jump = True
            fail = False
         elif check:
            jump = False
            fail = False
         else:
            print("Invalid input!")
            jump = False
            fail = True
      
      #update board
      move_piece(coords, player, jump)

      #test end condition
      test = 0
      for i in range(4):
         if board[5][i] == 1:
            test += 1
      if test == 4:
         running = False
         winner = 1
      
      disp_board()
      test = 0
      for i in range(4):
         if board[0][i] == 1:
            test += 1
      if test == 4:
         running = False   
         winner = 2
   print("Player " + str(winner) + " is the winner!")

game()
