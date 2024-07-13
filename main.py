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

def fill_deleted(row, pad=4, insert_in_front=False):
    padded = row
    while len(padded) != pad:
        if insert_in_front:
            padded.insert(0, None)
        else:
            padded.append(None)
    return padded

def shift_row(row, l_to_r):
    updated_row = [x for x in row if x is not None]
    done = False
    
    if l_to_r:
        i = len(updated_row) - 1
        while not done and i >= 1:
            curr = updated_row[i]
            prev = updated_row[i-1]
            if isCombinable(prev, curr):
                updated_row[i] = nextNumber(curr)
                del updated_row[i-1]
                done = True
            i -= 1
        
        fill_deleted(updated_row,insert_in_front=True)
    else:
        i = 0
        while not done and i+1 < len(updated_row):
            curr = updated_row[i]
            next = updated_row[i+1]
            if isCombinable(curr, next):
                updated_row[i] = nextNumber(curr)
                del updated_row[i+1]
                done = True
            i += 1
        fill_deleted(updated_row,insert_in_front=False)
    

    return updated_row

def player_move(board, input):
    match input.lower():
        case 'up':
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
assert(shift_row([None, 2, None, 2], True) == [None, None, None, 4])
assert(shift_row([2, 2, 2, 2], True) == [None, 2, 2, 4])
assert(shift_row([2, 2, 2, 2], False) == [4, 2, 2, None])



# print(shift_row([2, None, 2, 4], False))

# board = start_game()
# print(board)
# player_move(board, 'up')
# for i in range(15):
#     board = spawn_new_number_block(board)
#     print(board)