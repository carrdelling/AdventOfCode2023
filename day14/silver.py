
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


def calculate_load(grid):

    max_x = max(x[0] for x in grid)
    load = sum(max_x - i + 1 for (i, j), c in grid.items() if c == 'O')

    return load


def solve(data):

    grid = {}

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            grid[i, j] = c

    grid = move_north(grid)
    solution = calculate_load(grid)

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
