# define the board
board = [["_" for i in range(3)] for j in range(3)]

# EDIT: You can no longer override another player's move/you cannot make a move on a spot that is already taken. This change is found from lines 8 to 13.

# define the player's move
def make_move(board, player, row, col):
  if board[row][col] == "_":
    board[row][col] = player
    return True
  else:
    print("This spot is already taken. Try again.")
    return False

# define the function to check for a winner
def check_winner(board):
  # check rows
  for row in range(3):
    if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
      return board[row][0]

  # check columns
  for col in range(3):
    if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
      return board[0][col]

  # check diagonals
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
    return board[0][0]
  if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != "_":
    return board[2][0]

  # if there is no winner, return None
  return None

# define the function to check if the game is a draw
def check_draw(board):
  for row in range(3):
    for col in range(3):
      if board[row][col] == "_":
        return False
  return True

# define the function to play the game
def play_game():
  # initialize the game
  player = "X"
  winner = None
  draw = False

  # loop until the game is over
  while not winner and not draw:
    # print the current board
    for row in board:
      print(" ".join(row))

# EDIT: The game now announces who's turn it is after each move. This change can be found in line 62.

# EDIT: Instead of the range being from (0-2), I changed it to (1-3) because I find it less confusing when you are trying to make a move in the game. This can be found in lines 65 and 66, only the numbers were changed and a "-1" function was added.

    # get the player's move
    print(f"Player {player}'s turn")
    valid_move = False
    while not valid_move:
      row = int(input("Enter row (1-3): ")) - 1
      col = int(input("Enter column (1-3): ")) - 1
      valid_move = make_move(board, player, row, col)

    # check for a winner
    winner = check_winner(board)

    # check for a draw
    draw = check_draw(board)

    # switch players
    if player == "X":
      player = "O"
    else:
      player = "X"

  # print the final board
  for row in board:
    print(" ".join(row))

  # print the result of the game
  if winner:
    print(f"Player {winner} wins!")
  else:
    print("The game is a draw.")

# play the game
play_game()
