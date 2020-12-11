# write your code here
u_in = list(input('Enter cells:'))  # read the 9 symbol user input
line = '|'  # storing line in a variable
s = ' '
n_x = 0  # number of X's
n_o = 0  # number of O's
n_u = 0  # number of underscores
o_list = list('OOO')
x_list = list('XXX')
temp_list = list()
x_win = 0
o_win = 0
n_ele = 3  # number of elements


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
    next_move = input('Enter the coordinates:')
    next_move = next_move.strip()
    next_move = next_move.split(' ')
    if next_move[0].isdigit() != 1 or next_move[1].isdigit() != 1:
        print('You should enter numbers!')
        verify_coordinates()
    elif 3 < int(next_move[0]) or 3 < int(next_move[1]):
        print('Coordinates should be from 1 to 3!')
        verify_coordinates()
    elif u_in[3 * (3 - int(next_move[1])) + (int(next_move[0]) - 1)] != '_':
        print('This cell is occupied! Choose another one!')
        verify_coordinates()
    else:
        u_in[3 * (3 - int(next_move[1])) + (int(next_move[0]) - 1)] = 'X'

print_pattern(u_in)  # printing the pattern

verify_coordinates()

print_pattern(u_in)  # printing the pattern

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

#print("x win =", x_win, "o win =", o_win, "n underline =", n_u)
# Printing the results
#if x_win == 1 and o_win == 1 or abs(n_x - n_o) >= 2:
#    print("Impossible")
#elif x_win == 1:
#    print("X wins")
#elif o_win == 1:
#    print("O wins")
#elif n_u == 0:
#    print("Draw")
#else:
#    print("Game not finished")
