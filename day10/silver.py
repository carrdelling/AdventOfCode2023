from collections import defaultdict


def moves(point, area):

    if area[point] in {'|', 'L', 'J', 'S'} and area[(point[0] - 1, point[1])] in {'|', '7', 'F', 'S'}:
        yield point[0] - 1, point[1]

    if area[point] in {'|', 'F', '7', 'S'} and area[(point[0] + 1, point[1])] in {'|', 'J', 'L', 'S'}:
        yield point[0] + 1, point[1]

    if area[point] in {'-', '7', 'J', 'S'} and area[(point[0], point[1] - 1)] in {'-', 'F', 'L', 'S'}:
        yield point[0], point[1] - 1

    if area[point] in {'-', 'F', 'L', 'S'} and area[(point[0], point[1] + 1)] in {'-', 'J', '7', 'S'}:
        yield point[0], point[1] + 1


def solve(data):

    area = defaultdict(lambda: '.')
    start = None
    for x, row in enumerate(data):
        for y, c in enumerate(row):
            if c == '.':
                continue
            area[(x, y)] = c
            if c == 'S':
                start = x, y

    # just do a loop
    current = start
    prev = None
    steps = 0

    while (current != start) or steps == 0:
        for move in moves(current, area):
            if move != prev:
                prev = current
                current = move
                steps += 1
                break

    solution = steps // 2

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


