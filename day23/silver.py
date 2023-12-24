

def moves(current, field):

    x, y = current

    # north
    if field[x-1][y] == '^':
        yield (x-2, y), 2
    if field[x-1][y] == '>':
        yield (x-1, y+1), 2
    if field[x-1][y] == '<':
        yield (x-1, y-1), 2
    if field[x-1][y] == '.':
        yield (x-1, y), 1

    # south
    if field[x+1][y] == 'v':
        yield (x+2, y), 2
    if field[x+1][y] == '>':
        yield (x+1, y+1), 2
    if field[x+1][y] == '<':
        yield (x+1, y-1), 2
    if field[x+1][y] == '.':
        yield (x+1, y), 1

    # left
    if field[x][y-1] == '^':
        yield (x-1, y-1), 2
    if field[x][y-1] == 'v':
        yield (x+1, y-1), 2
    if field[x][y-1] == '<':
        yield (x, y-2), 2
    if field[x][y-1] == '.':
        yield (x, y-1), 1

    # right
    if field[x][y+1] == '^':
        yield (x-1, y+1), 2
    if field[x][y+1] == 'v':
        yield (x+1, y+1), 2
    if field[x][y+1] == '>':
        yield (x, y+2), 2
    if field[x][y+1] == '.':
        yield (x, y+1), 1


def solve(data):

    field = []

    for i, row in enumerate(data):
        new_row = tuple(x for x in row)
        field.append(new_row)

    start = 0, 1
    goal = 140, 139

    max_steps = 0
    visited = frozenset([start])
    start_state = (0, start, visited)

    states = [start_state]

    while states:
        steps, loc, fvisisted = states.pop()

        if loc == goal:
            max_steps = max(max_steps, steps)
            continue

        visited = set(fvisisted)

        for new_loc, cost in moves(loc, field):
            if new_loc not in visited:
                new_steps = steps + cost
                new_visited = visited.copy()
                new_visited.add(new_loc)

                new_state = (new_steps, new_loc, frozenset(new_visited))
                states.append(new_state)

    solution = max_steps

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


