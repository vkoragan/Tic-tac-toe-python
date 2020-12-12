u_in = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
o_list = list('OOO')
x_list = list('XXX')
x_win = 0
o_win = 0
n_ele = 3  # number of elements
count = 2
move = ['-']

def print_pattern(field):   # function for printing the tic tac toe stage
    d = '-'                 # storing dash in a variable
    print(d * 9)            # print the first dashes line
    for i in range(0, len(field), n_ele):
        temp = ['|']
        for j in range(i, i + n_ele):
            temp = temp + list(field[j])
        temp = temp + ['|']
        print(" ".join(temp).replace("_", " "))
    print(d * 9)            # print the bottom dashes line


def verify_coordinates():
    global move
    global u_in
    next_move = input('Enter the coordinates:')
    next_move = next_move.strip()
    next_move = next_move.split(' ')
    if next_move[0].isdigit() != 1 or next_move[1].isdigit() != 1:
        print('You should enter numbers!')
        verify_coordinates()
    elif 3 < int(next_move[0]) or 3 < int(next_move[1]):
        print('Coordinates should be from 1 to 3!')
        verify_coordinates()
    elif u_in[-4 + int(next_move[0]) * 3 + int(next_move[1])] != '_':
        print('This cell is occupied! Choose another one!')
        verify_coordinates()
    else:
        u_in[-4 + int(next_move[0]) * 3 + int(next_move[1])] = move[0]


def winner_check():
    global x_win
    global o_win
    n_x = 0  # number of X's
    n_o = 0  # number of O's
    n_u = 0  # number of underscores

    # counting the number of X, O and _
    for j in u_in:
        if j == 'X':
            n_x += 1
        elif j == 'O':
            n_o += 1
        else:
            n_u += 1

    # checking wins across rows
    for i in range(0, len(u_in), n_ele):    # generic code, will work for tic tac toe of any size
        temp_list = list()
        for j in range(i, i + n_ele):
            temp_list.append(u_in[j])
        if temp_list == x_list:
            x_win += 1
        elif temp_list == o_list:
            o_win += 1

    # to check wins across columns
    for i in range(0, n_ele):
        temp_list = list()
        for j in range(i, len(u_in), 3):
            temp_list.append(u_in[j])
        if temp_list == x_list:
            x_win += 1
        elif temp_list == o_list:
            o_win += 1

    # to check wins across diagonals
    for i in range(1):
        temp_list = list()
        for j in range(i, len(u_in), n_ele + 1):    # diagonal from left to right
            temp_list.append(u_in[j])
        if temp_list == x_list:
            x_win += 1
        elif temp_list == o_list:
            o_win += 1
        temp_list = list()
        for j in range(len(u_in) - n_ele, 0, -(n_ele - 1)):     # diagonal from right to left
            temp_list.append(u_in[j])
        if temp_list == x_list:
            x_win += 1
        elif temp_list == o_list:
            o_win += 1
    return()


def the_game():
    global u_in
    global x_win
    global o_win
    global count
    winner_check()
    if x_win == 1 or o_win == 1:
        return()
    else:
        if count % 2 == 0:
            move[0] =  'X'
            verify_coordinates()
            print_pattern(u_in)
            count += 1
            the_game()
        else:
            move[0] = 'O'
            verify_coordinates()
            print_pattern(u_in)
            count += 1
            the_game()


# printing the empty pattern
print_pattern("".join(u_in).replace("_", " "))
the_game()

if x_win == 1:
    print('X wins')
else:
    print('O wins')
