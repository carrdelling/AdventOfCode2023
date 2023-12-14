
def move_north(grid):

    changes = True

    while changes:
        changes = False
        for (i, j), c in grid.items():
            if c == 'O' and i > 0 and grid[(i-1, j)] == '.':
                grid[(i - 1, j)] = 'O'
                grid[(i, j)] = '.'
                changes = True

    return grid


def move_south(grid):

    max_x = max(x[0] for x in grid)
    changes = True

    while changes:
        changes = False
        for (i, j), c in grid.items():
            if c == 'O' and i < max_x and grid[(i+1, j)] == '.':
                grid[(i + 1, j)] = 'O'
                grid[(i, j)] = '.'
                changes = True

    return grid


def move_west(grid):

    changes = True

    while changes:
        changes = False
        for (i, j), c in grid.items():
            if c == 'O' and j > 0 and grid[(i, j-1)] == '.':
                grid[(i, j - 1)] = 'O'
                grid[(i, j)] = '.'
                changes = True

    return grid


def move_east(grid):
    max_y = max(x[1] for x in grid)
    changes = True

    while changes:
        changes = False
        for (i, j), c in grid.items():
            if c == 'O' and j < max_y and grid[(i, j + 1)] == '.':
                grid[(i, j + 1)] = 'O'
                grid[(i, j)] = '.'
                changes = True

    return grid


def do_cycle(grid):

    grid = move_north(grid)
    grid = move_west(grid)
    grid = move_south(grid)
    grid = move_east(grid)

    return grid


def calculate_load(grid):

    max_x = max(x[0] for x in grid)
    load = sum(max_x - i + 1 for (i, j), c in grid.items() if c == 'O')

    return load


def calculate_load_hashed_grid(h_grid, n_cols):

    grid = {}

    for idx, c in enumerate(h_grid):
        i = idx // n_cols
        j = idx % n_cols
        grid[(i, j)] = c

    return calculate_load(grid)


def solve(data):

    TARGET = 1000000000
    grid = {}

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            grid[i, j] = c

    n_cols = len(data[0])

    seen = {}
    offset = - 1
    cycle_len = -1
    for i in range(1, TARGET):
        grid = do_cycle(grid)
        h = ''.join([c for (i, j), c in sorted(grid.items())])
        if h in seen:
            cycle_len = i - seen[h]
            offset = seen[h]
            break
        else:
            seen[h] = i

    key = (offset + (TARGET - offset) % cycle_len)
    h = [g for g, k in seen.items() if k == key][0]

    solution = calculate_load_hashed_grid(h, n_cols)

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row.strip()
            input_.append(v)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
