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
    all_points = set()
    start = None
    for x, row in enumerate(data):
        for y, c in enumerate(row):
            all_points.add((x, y))
            if c == '.':
                continue
            area[(x, y)] = c
            if c == 'S':
                start = x, y

    # just do a loop
    current = start
    prev = None
    steps = 0

    visited = set()

    while (current != start) or steps == 0:
        visited.add(current)
        for move in moves(current, area):
            if move != prev:
                prev = current
                current = move
                steps += 1
                break

    inside = 0
    for point in all_points:
        if point in visited:
            continue
        # for each point not in the main loop, count how many 'columns'
        # do we need to cross to reach it. Odd columns: inside
        columns = 0
        for i in range(point[1]):
            middle_point = point[0], i
            if middle_point in visited and area[middle_point] in {'|', 'J', 'L', 'S'}:
                columns += 1

        if columns % 2 == 1:
            inside += 1

    solution = inside

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
