
def solve(data):

    ins = []

    for row in data:
        chunks = row.split()
        ins.append((chunks[0], int(chunks[1]), chunks[2]))

    area = set()

    current = 0, 0
    area.add(current)

    dirs = {
        'R': (0, 1),
        'L': (0, -1),
        'D': (1, 0),
        'U': (-1, 0),
    }

    # perimeter
    max_x, max_y, min_x, min_y = 0, 0, 0, 0
    for direction, length, _ in ins:

        move = dirs[direction]

        for i in range(length):
            current = current[0] + move[0], current[1] + move[1]
            area.add(current)

            min_x = min(min_x, current[0])
            min_y = min(min_y, current[1])
            max_x = max(max_x, current[0])
            max_y = max(max_y, current[1])

    # floodfill
    current = (min_x + max_x) // 2, (min_y + max_y) // 2

    to_flood = [current]

    while to_flood:
        current = to_flood.pop()

        area.add(current)

        for move in dirs.values():
            neig = current[0] + move[0], current[1] + move[1]
            if neig not in area:
                area.add(neig)
                to_flood.append(neig)

    solution = len(area)

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
