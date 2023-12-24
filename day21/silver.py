from collections import deque


def solve(data):

    garden = set()

    start = None
    for i, row in enumerate(data):
        for j, c in enumerate(row):

            if c == 'S':
                start = i, j
            if c == '#':
                garden.add((i, j))

    max_x = len(data)
    max_y = len(data[0])

    initial = (start[0], start[1], 0)
    states = deque([initial])

    reached = {}
    while states:
        x, y, s = states.popleft()

        if s > 64:
            continue

        if (x, y) in reached:
            continue

        if s % 2 == 0:
            reached[(x, y)] = s

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy

            if (0 <= nx < max_x) and (0 <= y < max_y) and (nx, ny) not in garden:
                states.append((nx, ny, s+1))

    solution = len(reached)

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
