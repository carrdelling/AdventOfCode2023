from collections import deque


def count(garden, steps, start_steps, size):

    initial = (65, 65, start_steps)
    states = deque([initial])

    reached = {}
    while states:
        x, y, s = states.popleft()

        if s > steps:
            continue

        if (x, y) in reached:
            continue

        if s % 2 == 0:
            reached[(x, y)] = s

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            fx = x + dx
            fy = y + dy
            nx = (fx + size) % size
            ny = (fy + size) % size

            if (nx, ny) not in garden:
                states.append((fx, fy, s + 1))

    return len(reached)


def solve(data):

    garden = set()

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == '#':
                garden.add((i, j))

    size = len(data)
    to_border = size // 2

    one_grid = count(garden, to_border, -1, size)
    two_grids = count(garden, to_border + size, 0, size)
    three_grids = count(garden, to_border + size + size, -1, size)

    # quadratic form
    a = (three_grids - 2 * two_grids + one_grid) // 2
    b = two_grids - one_grid - a
    c = one_grid

    n = (26501365 - to_border) // size
    solution = a * n ** 2 + b * n + c

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
