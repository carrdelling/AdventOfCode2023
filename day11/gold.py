from itertools import combinations


def solve(data):
    area = set()

    max_x = -1
    max_y = -1

    for x, row in enumerate(data):
        for y, c in enumerate(row):
            if c == '.':
                continue
            max_x = max(x, max_x)
            max_y = max(y, max_y)
            area.add((x, y))

    normal_x = {x[0] for x in area}
    normal_y = {x[1] for x in area}
    expand_r = {x for x in range(max_x + 1) if x not in normal_x}
    expand_c = {y for y in range(max_y + 1) if y not in normal_y}

    points = sorted(area)

    full_dist = 0
    expansion = 1000000 - 1
    for (x1, y1), (x2, y2) in combinations(points, r=2):
        x1, x2 = min(x1, x2), max(x1, x2)
        y1, y2 = min(y1, y2), max(y1, y2)

        dist = (x2 - x1)
        dist += sum(expansion for x in range(x1, x2 + 1) if x in expand_r)
        dist += (y2 - y1)
        dist += sum(expansion for x in range(y1, y2 + 1) if x in expand_c)

        full_dist += dist

    solution = full_dist

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
