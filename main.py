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

def shift_row(row, shift_left):
    updated_row = row
    done = False
    if shift_left:
        updated_row.reverse()
    
    # process left to right
    for i in range(len(updated_row)):
        if not done and i + 1 < len(updated_row):
            curr = updated_row[i]
            next = updated_row[i+1]
            print(curr, next)
            if isCombinable(curr, next):
                updated_row[i+1] = nextNumber(curr)
                updated_row.remove(i)
                updated_row.insert(0, None)
                done = True
            elif next is None:
                # fix bug, when 2 None 2 4 should become None None 4 4 
                updated_row[i+1] = curr
                print(i)
                
                print(updated_row)
                # updated_row.remove(i)
                # updated_row.insert(0, None)

    if shift_left:
        updated_row.reverse()
    
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


print(shift_row([2, None, 2, 4], False))
# board = start_game()
# print(board)
# player_move(board, 'up')
# for i in range(15):
#     board = spawn_new_number_block(board)
#     print(board)