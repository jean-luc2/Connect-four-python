board = [['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0'], ['0', '0', '0', '0', '0', '0']]
X = 'X'
O = 'O'
def print_board():
  for row in board:
    print(row)
  return ''

def horizontal_check():
  num1 = 0
  num2 = 1
  num3 = 2
  num4 = 3
  for row in board: 
    if row[num1] == 'X' and row[num2] == 'X' and row[num3] == 'X' and row[num4] == 'X':
      print('X wins!')
    num1 += 1
    num2 += 1
    num3 += 1
    num4 += 1

while True:
  print(print_board())
  INPUT = int(input("Enter your column to play in: "))-1
  for i in range(5,-1,-1):
    
    if board[i][INPUT] == '0':
      board[i][INPUT] = 'X'
      break
  horizontal_check()
