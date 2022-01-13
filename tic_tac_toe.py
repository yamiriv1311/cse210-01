
"""
Assignment: Tic-Tac-Toe game
Author: Yamileth Rivero Garcia
"""

def main():
  print()
  print("Welcome to the best Tic-Tac-Toe game app!")
  player1 = input("First player, please type your username: ")
  player2 = input("Second player, please type your username: ")
  print()
  print(f"Nice to meet you {player1.capitalize()} and {player2.capitalize()}")
  print(f"{player1.capitalize()} you are going to use X's, {player2.capitalize()} you are going to use O's")
  print("Let's start!")

  board = game_board()
  player = change_player("")

  while not (winner(board) or draw(board)):
    see_lines(board)
    next_turn(player, board)
    player = change_player(player)
  see_lines(board)
  print("Nice play!!")

  #Also, this didn't worked out:
  """if winner == "X":
    print(f"{player1.capitalize()} won!")
  elif winner == "O":
    print(f"{player2.capitalize()} won!")
  elif winner == None:
    print(f"Tie :D -- {player1.capitalize()} and {player2.capitalize()} both are so good at tic tac toe!")
"""

def game_board():
  lines = []
  for each_space in range(9):
    lines.append(each_space + 1)
  return lines

def see_lines(lines):
  print()
  print(f" {lines[0]} | {lines[1]} | {lines[2]}")
  print("---+---+---")
  print(f" {lines[3]} | {lines[4]} | {lines[5]}")
  print("---+---+---")
  print(f" {lines[6]} | {lines[7]} | {lines[8]}")

def next_turn(player, lines):
  choosed_number = int(input(f"\n{player} choose a number from 1-9 ant type it: "))
  choosed_number = choosed_number - 1
  lines[choosed_number] = player

def winner(lines):
  #To check if someone wins, we need to check all possible ways to win, we now 3
  #ways to win: by having same symbols in rows, columns and in a diagonal form.

  #Let's check the rows first
  """way_to_win1 = lines[0] == lines[1] == lines[2] 
  way_to_win2 = lines[3] == lines[4] == lines[5] 
  way_to_win3 = lines[6] == lines[7] == lines[8] 
  #Now let's check the columns
  way_to_win4 = lines[0] == lines[3] == lines[6] 
  way_to_win5 = lines[1] == lines[4] == lines[7] 
  way_to_win6 = lines[2] == lines[5] == lines[8] 
  #To end, let's check the diagonal lines
  way_to_win7 = lines[0] == lines[4] == lines[8] 
  way_to_win8 = lines[2] == lines[4] == lines[6] 

  if way_to_win1 or way_to_win2 or way_to_win3 or way_to_win4 or way_to_win5 or way_to_win6 or way_to_win7 or way_to_win8:
    print("You win!")
  
  #This is to return the winner, either X's or O's
  if way_to_win1:
    winner = lines[0]
    return winner
  elif way_to_win2:
    winner = lines[3]
    return winner
  elif way_to_win3:
    winner = lines[6]
    return winner
  elif way_to_win4:
    winner = lines[0]
    return winner
  elif way_to_win5:
    winner = lines[1]
    return winner
  elif way_to_win6:
    winner = lines[2]
    return winner
  elif way_to_win7:
    winner = lines[0]
    return winner
  elif way_to_win8:
    winner =  lines[2]
    return winner"""
      #I tried but that previuos stuff did't work
      
  return (lines[0] == lines[1] == lines[2] or
          lines[3] == lines[4] == lines[5] or
          lines[6] == lines[7] == lines[8] or
          lines[0] == lines[3] == lines[6] or
          lines[1] == lines[4] == lines[7] or
          lines[2] == lines[5] == lines[8] or
          lines[0] == lines[4] == lines[8] or
          lines[2] == lines[4] == lines[6])

def draw(lines):
  for each_space in range(9):
    if lines[each_space] != "X" and lines[each_space] != "O":
      return False
  return True


def change_player(current_player):
  if current_player == "" or current_player == "O":
    return "X"
  elif current_player == "X":
    return "O"
  
  
main()