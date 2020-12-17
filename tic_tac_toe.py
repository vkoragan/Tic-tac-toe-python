board = list()  # captures the state of the tic tac toe board
o_list = list()  # variable that sores the winning pattern for O
x_list = list()  # variable that sores the winning pattern for X
x_win = False
o_win = False
count = 0
move = ['-']  # variable that holds the current move. X or O


def generate_board():
    global board
    global o_list
    global x_list
    global dimension_board
    for _ in range(0, dimension_board ** 2):  # creates an empty board
        board = board + ['_']
    for _ in range(0, dimension_board):
        o_list = o_list + ["O"]
        x_list = x_list + ["X"]


def print_pattern(field):
    # function for printing the tic tac toe stage
    print('_' * (3 + dimension_board * 2))            # print the first dashes line
    for i in range(0, len(field), dimension_board):
        temp = ['|']
        for j in range(i, i + dimension_board):
            temp = temp + list(field[j])
        temp = temp + ['|']
        print(" ".join(temp).replace("_", " "))
    print('_' * (3 + dimension_board * 2))       # print the bottom dashes line


def verify_coordinates(user):
    # function to verify if a cell's availability and assign move
    global move
    global board
    next_move = input(f'Enter the coordinates for user {user}: ')
    next_move = next_move.strip()
    next_move = next_move.split(' ')
    if next_move[0].isdigit() != 1 or next_move[1].isdigit() != 1:
        print('You should enter numbers!')
        verify_coordinates(user)
    elif dimension_board < int(next_move[0]) or dimension_board < int(next_move[1]):
        print(f'Coordinates should be from 1 to {dimension_board}!')
        verify_coordinates(user)
    elif board[int(next_move[0]) * dimension_board + int(next_move[1]) - (dimension_board + 1)] != '_':
        print('This cell is occupied! Choose another one!')
        verify_coordinates(user)
    else:
        board[int(next_move[0]) * dimension_board + int(next_move[1]) - (dimension_board + 1)] = move[0]


def winner_check():
    # function to check if there's a winner or
    global x_win
    global o_win

    # checking wins across rows
    for i in range(0, len(board), dimension_board):    # generic code, will work for tic tac toe of any size
        temp_list = list()
        for j in range(i, i + dimension_board):
            temp_list.append(board[j])
        if temp_list == x_list:
            x_win = True
        elif temp_list == o_list:
            o_win = True

    # to check wins across columns
    for i in range(0, dimension_board):
        temp_list = list()
        for j in range(i, len(board), dimension_board):
            temp_list.append(board[j])
        if temp_list == x_list:
            x_win = True
        elif temp_list == o_list:
            o_win = True

    # to check wins across diagonals
    for i in range(1):
        temp_list = list()
        for j in range(i, len(board), dimension_board + 1):    # diagonal from left to right
            temp_list.append(board[j])
        if temp_list == x_list:
            x_win = True
        elif temp_list == o_list:
            o_win = True
        temp_list = list()
        for j in range(len(board) - dimension_board, 0, -(dimension_board - 1)):     # diagonal from right to left
            temp_list.append(board[j])
        if temp_list == x_list:
            x_win = True
        elif temp_list == o_list:
            o_win = True
    return()


def the_game():  # recursive function that executes until there's win or all the cells are filled
    global board
    global x_win
    global o_win
    global count
    winner_check()
    if x_win == 1 or o_win == 1 or count == (dimension_board ** 2):
        return()
    else:
        if count % 2 == 0 and count != 1:
            move[0] = 'X'
            verify_coordinates(move[0])
            print_pattern(board)
            count += 1
            the_game()
        else:
            move[0] = 'O'
            verify_coordinates(move[0])
            print_pattern(board)
            count += 1
            the_game()


# printing the empty pattern
dimension_board = int(input("Enter no. of rows for the tic tac toe board \n("
                            "should not be less than 3): "))  # dimension of the tic tac toe board
generate_board()
print(board)
print(x_list, o_list)
print_pattern("".join(board).replace("_", " "))
the_game()

if x_win:
    print('X wins')
elif o_win:
    print('O wins')
else:
    print('Draw')
