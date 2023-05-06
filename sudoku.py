import copy
import numpy

grid = [[0, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 6, 0, 0, 0, 0, 3],
        [0, 7, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 3, 0, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [6, 0, 0, 5, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 7, 8, 0],
        [5, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 0]]


print("sudoku solver started")
root_grid = copy.deepcopy(grid)
rows = len(grid)
columns = len(grid[0])
print(f"rows: {rows}, columns: {columns}")
elements = [ele+1 for ele in range(9)]
steps = 0
# prioritize_single = True
# multi_attempted = False
# attempt_fail = False
# threshold = 2

def correctness_check(matrix):
    for row, cur_row in enumerate(matrix):
        for position, element in enumerate(cur_row):
            cur_col = [val[position] for val in matrix]
            sub_matrix = subset_position(matrix, row, position)
            if not (sum(cur_row) == sum(cur_col) == sum(sub_matrix) == 45): 
                print("correctness check failed")
                return False   
    return True

def subset_position(matrix, row_num, position):
    row_set, col_set = [], []
    subcol = position%3
    if subcol == 0: col_neighbour = [position, position+1, position+2]
    elif subcol == 2: col_neighbour = [position-2, position-1, position]
    else: col_neighbour = [position-1, position, position+1]

    subrow = row_num%3
    if subrow == 0: row_neighbour = [row_num, row_num+1, row_num+2]
    elif subrow == 2: row_neighbour = [row_num-2, row_num-1, row_num]
    else: row_neighbour = [row_num-1, row_num, row_num+1]

    for row in row_neighbour:
        for col in col_neighbour:
            row_set.append(row)
            col_set.append(col)

    np_arr = numpy.array(matrix)
    return np_arr[[row_set], [col_set]].flatten()


def completion_check(matrix):
    np_arr = numpy.array(matrix)
    if 0 in np_arr or matrix is None: return False
    else: return True

# def solve(matrix):
#     global tmp_matrix
#     global grid
#     global threshold

#     global attempt_fail
#     global multi_attempted
#     global prioritize_single
#     cycle_threshold = 2

#     for num in range(9):
#         cur_row = matrix[num]

#         for position, element in enumerate(cur_row):
#             if element == 0:
#                 cur_col = [val[position] for val in matrix]
#                 sub_matrix = subset_position(matrix, num, position)
#                 possible_elements = list(numpy.setdiff1d(elements, list(set().union(cur_row, cur_col, sub_matrix))))
#                 cycle_threshold = len(possible_elements) if len(possible_elements) > 2 and len(possible_elements) <= cycle_threshold else cycle_threshold
#                 if len(possible_elements) > 0:
#                     print(f"potential elements for position: [{num}]*[{position}] is {possible_elements}")
#                     if len(possible_elements) == 1:
#                         print(f"applying for position: [{num}]*[{position}] with value {possible_elements[0]}")
#                         matrix[num][position] = possible_elements[0]
#                         if prioritize_single and not multi_attempted: return matrix
#                         else: matrix = solve(matrix)            
#                     elif not prioritize_single and len(possible_elements) == cycle_threshold:
#                         multi_attempted = True
#                         if not attempt_fail: possible_element = possible_elements[0]
#                         else:
#                             possible_element = possible_elements[1]
#                             attempt_fail = False
#                         print(f"attempting for position: [{num}]*[{position}] with value {possible_element}")
#                         tmp_matrix = copy.deepcopy(matrix)
#                         matrix[num][position] = possible_element
#                         prioritize_single = True
#                         matrix = solve(matrix)
#                         if completion_check(matrix):
#                             if correctness_check(matrix): return matrix
#                         else: continue
#                 else:
#                     print(f"attempt failed during calculation of position: [{num}]*[{position}], reverting to original matrix")
#                     attempt_fail = True
#                     prioritize_single = False
#                     solve(tmp_matrix)
#     prioritize_single = False
#     matrix = solve(matrix)


def processer(matrix, row, col):
    global steps
    steps += 1
    if (row == rows-1 and col == columns): 
        if completion_check(matrix) and correctness_check(matrix): return True
    if col == columns: 
        row += 1
        col = 0
    if matrix[row][col] != 0: return processer(matrix, row, col+1)

    sub_matrix = subset_position(matrix, row, col)
    cur_row = matrix[row]
    cur_col = [val[col] for val in matrix]
    possible_elements = list(numpy.setdiff1d(elements, list(set().union(cur_row, cur_col, sub_matrix))))
    for possible_num in possible_elements:
        grid[row][col] = possible_num
        if processer(grid, row, col + 1):
            return True
        matrix[row][col] = 0
    return False


if processer(grid, 0, 0):
    print(f"sudoku solver completed, steps taken: {steps}")

    print("\n\n+ ----------- + ----------- + ----------- +", end="")
    for row in range(rows):
        print("\n",end="\n|  ")
        for col in range(columns):
            num_end = "  |  " if ((col+1)%3 == 0) else "   "
            print(grid[row][col],end=num_end)
        
        if ((row+1)%3 == 0):
            print("\n\n+ ----------- + ----------- + ----------- +", end="")