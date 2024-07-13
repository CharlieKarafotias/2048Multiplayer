import random

# Board logic
def isCombinable(a, b):
    if a is not None and b is not None:
        return a == b
    else:
        return False

def nextNumber(a):
    return a*2

def hasWon(board):
    return 2048 in board

# Game logic
def start_game():
    initial_board = [None] * 16
    # generate 2 numbers 
    num_1 = random.randint(0,15)
    num_2 = random.randint(0,15)
    while num_1 == num_2:
        num_2 = random.randint(0,15)
    initial_board[num_1] = 2
    initial_board[num_2] = 2
    return initial_board

def spawn_new_number_block(board):
    available_spots = []
    for (idx, elem) in enumerate(board):
        if elem is None:
            available_spots.append(idx)
    
    if available_spots:
        idx_on_board_to_update = random.randint(0,len(available_spots)-1)
        board[available_spots[idx_on_board_to_update]] = 2
    return board

def fill_deleted(row, pad=4):
    padded = row
    while len(padded) != pad:
        padded.append(None)
    return padded

def shift_row(row, shift_right):
    updated_row = row
    if shift_right:
        updated_row.reverse()
    
    done = False
    i = 0
    while not done:
        if len(updated_row) <= i:
                done = True
                break
        curr = updated_row[i]
        print(updated_row, curr, i)
        if curr is None:
            del updated_row[i]
        elif len(updated_row) > i+1 and isCombinable(curr, updated_row[i+1]):
            updated_row[i] = nextNumber(curr)
            del updated_row[i+1]
        elif len(updated_row) > i+1:
            i += 1
        else:
            # out of elements or cant combine
            done = True

    fill_deleted(updated_row)

    if shift_right:
        updated_row.reverse()
    
    print(updated_row)
    
    return updated_row

def player_move(board, input):
    match input.lower():
        case 'up':
            # [2, None, None, None, None, 2, None, None, None, None, None, None, None, None, None, None]
            print(board)
            columns = [[], [], [], []]
            for (idx, elem) in enumerate(board):
                column_to_add_to = columns[idx % 4]
                column_to_add_to.append(elem)
            print(columns)
        case 'down':
            columns = [[]] * 4
            for (idx, elem) in enumerate(board):
                columns[idx % 4] = columns[idx % 4].append(elem)
        case 'left':
            pass
        case 'right':
            pass
    return board

# Graphics
def print_board(board, split_on=4):
    rows = []
    while board:
        rows.append(board[:split_on])
        del board[:split_on]
    for r in rows:
        print(r)
    


assert(shift_row([None, None, None, None], True) == [None, None, None, None])
assert(shift_row([2, None, None, None], True) == [None, None, None, 2])
assert(shift_row([2, 2, None, None], True) == [None, None, None, 4])
assert(shift_row([2, 4, None, None], True) == [None, None, 2, 4])
print('failing cases:')
assert(shift_row([None, 2, None, 2], True) == [None, None, None, 4])
# assert(shift_row([2, 2, 2, 2], True) == [None, 2, 2, 4])


# print(shift_row([2, None, 2, 4], False))

# board = start_game()
# print(board)
# player_move(board, 'up')
# for i in range(15):
#     board = spawn_new_number_block(board)
#     print(board)