u_in = list(input())  # read the 9 symbol user input
d = '-'  # storing dash in a variable
line = '|'  # storing line in a variable
s = ' '

# print the first dashes line
print(d * 9)

# print the tic tac toe pattern
print(line, u_in[0], u_in[1], u_in[2], line)
print(line, u_in[3], u_in[4], u_in[5], line)
print(line, u_in[6], u_in[7], u_in[8], line)

# print the bottom dashes line
print(d * 9)
n_x = 0  # number of X's
n_o = 0  # number of O's
n_u = 0  # number of underscores
o_list = list('OOO')
x_list = list('XXX')
temp_list = list()
x_win = 0
o_win = 0
n_ele = 3  # number of elements

# counting the number of X, O and _
for j in u_in:
    if j == 'X':
        n_x += 1
    elif j == 'O':
        n_o += 1
    else:
        n_u += 1

# checking wins across rows
for i in range(0, len(u_in), n_ele):    # generic code will work for tic tac toe of any size
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

print("x win =", x_win, "o win =", o_win, "n underline =", n_u)
# Printing the results
if x_win == 1 and o_win == 1 or abs(n_x - n_o) >= 2:
    print("Impossible")
elif x_win == 1:
    print("X wins")
elif o_win == 1:
    print("O wins")
elif n_u == 0:
    print("Draw")
else:
    print("Game not finished")