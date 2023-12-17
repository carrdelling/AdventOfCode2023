

def switch(current, direction, grid):

    new_direction = None
    new_current = None
    another_direction = None
    another_current = None

    if grid[current] == '.':
        new_direction = direction
        new_current = current[0] + new_direction[0], current[1] + new_direction[1]

    elif grid[current] == '/':
        new_direction = {(-1, 0): (0, 1),
                         (1, 0): (0, -1),
                         (0, 1): (-1, 0),
                         (0, -1): (1, 0)}[direction]
        new_current = current[0] + new_direction[0], current[1] + new_direction[1]

    elif grid[current] == '\\':
        new_direction = {(-1, 0): (0, -1),
                         (1, 0): (0, 1),
                         (0, 1): (1, 0),
                         (0, -1): (-1, 0)}[direction]
        new_current = current[0] + new_direction[0], current[1] + new_direction[1]

    elif grid[current] == '|':
        if direction in {(-1, 0), (1, 0)}:
            new_direction = direction
            new_current = current[0] + new_direction[0], current[1] + new_direction[1]
        elif direction in {(0, -1), (0, 1)}:
            new_direction = (-1, 0)
            new_current = current[0] + new_direction[0], current[1] + new_direction[1]
            another_direction = (1, 0)
            another_current = current[0] + another_direction[0], current[1] + another_direction[1]
    elif grid[current] == '-':
        if direction in {(0, -1), (0, 1)}:
            new_direction = direction
            new_current = current[0] + new_direction[0], current[1] + new_direction[1]
        elif direction in {(-1, 0), (1, 0)}:
            new_direction = (0, -1)
            new_current = current[0] + new_direction[0], current[1] + new_direction[1]
            another_direction = (0, 1)
            another_current = current[0] + another_direction[0], current[1] + another_direction[1]
    else:
        pass

    return (new_current, new_direction), (another_current, another_direction)


def solve(data):

    grid = {}

    max_x, max_y = 0, 0
    for i, row in enumerate(data):
        max_x = max(max_x, i)
        for j, c in enumerate(row):
            grid[i, j] = c
            max_y = max(max_y, j)

    beam = 0, 0
    direction = 0, 1
    beams = [(beam, direction)]
    seen = set()

    while beams:

        beam = beams.pop()

        if beam in seen:
            continue

        seen.add(beam)
        orig_beam, new_beam = switch(*beam, grid)

        for beam in (orig_beam, new_beam):
            if beam[0] is None:
                continue

            # normal exit
            if not ((0 <= beam[0][0] <= max_x) and (0 <= beam[0][1] <= max_y)):
                continue

            beams.append(beam)

    solution = len({x[0] for x in seen})

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
