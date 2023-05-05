# TASK 15 MINESWEEPER TASK

# (1) Import required modules here.

from pprint import pprint

# (2) Define the constants which are the minesweeper grid and the definition of the neighbouring cells.

EXAMPLE = [["-", "-", "-", "#", "#"],
           ["-", "#", "-", "-", "-"],
           ["-", "-", "#", "-", "-"],
           ["-", "#", "#", "-", "-"],
           ["-", "-", "-", "-", "-"]]

NEIGHBOURS = [(-1, -1), (0, -1), (1, -1),
              (-1, 0), (0, 0), (1, 0),
              (-1, 1), (0, 1), (1, 1)]

# (3) Create a function that counts the number of mines around a particular grid location.

def count_all_mines(mine_map):
    mine_counts = []
    for row_number, row in enumerate(mine_map):
        new_row = [count_neighbours(row_number, col_number, mine_map) for col_number, col in enumerate(row)]
        mine_counts.append(new_row)
    return mine_counts

# (4) Create a function that delivers a string of the count of the mines in the adjacent cells.

def count_neighbours(row_number, col_number, mine_map):
    count = 0
    if mine_map[row_number][col_number] == "#":
        return "#"
    for dc, dr in NEIGHBOURS:
        r, c = row_number + dr, col_number + dc
        if r < 0 or c < 0:
            continue
        try:
            count += 1 if mine_map[r][c] == "#" else 0
        except IndexError:
            pass
    return str(count)

result = count_all_mines(EXAMPLE)
pprint(result)
