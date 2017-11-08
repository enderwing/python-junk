import random
def add_values(values):
  while '0' in values:
    values.remove('0')

  new_values = []

  while len(values) > 1:
    if values[0] == values[1]:
      new_values.append(str(int(values[0])*2))
      values.pop(0)
      values.pop(0)
    else:
      new_values.append(values.pop(0))
  if len(values) == 1:
    new_values.append(values.pop())
  while len(new_values) < 4:
    new_values.append('0')

  return new_values

def rotate(matrix):
  return [[matrix[0][column],matrix[1][column],matrix[2][column],matrix[3][column]] for column in range(4)]

def pr_board(board):
  for row in board:
    for numb in row:
      print(numb,end=' ')
    print()

#board = [input().split(' ') for x in range(4)]
board = [[random.choice(['2','4','8','0']) for x in range(4)],[random.choice(['2','4','8','0']) for x in range(4)],[random.choice(['2','4','8','0']) for x in range(4)],[random.choice(['2','4','8','0']) for x in range(4)]]
pr_board(board)
dirr = input()

if dirr == '0': # left
  board = [add_values(board[row]) for row in range(4)]
  pr_board(board)

elif dirr == '1': # up
  board = rotate([add_values(rotate(board)[row]) for row in range(4)])
  pr_board(board)

elif dirr == '2': # right
  board = [add_values(board[row][::-1])[::-1] for row in range(4)]
  pr_board(board)

elif dirr == '3': # down
    board = rotate([add_values(rotate(board)[row][::-1])[::-1] for row in range(4)])
    pr_board(board)
