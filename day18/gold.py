
def solve(data):

    ins = []

    for row in data:
        chunks = row.split()
        ins.append((chunks[0], int(chunks[1]), chunks[2]))

    dirs = {
        '0': (0, 1),
        '2': (0, -1),
        '1': (1, 0),
        '3': (-1, 0),
    }

    # perimeter
    perimeter = set()
    current = 0, 0
    perimeter.add(current)
    max_x, max_y, min_x, min_y = 0, 0, 0, 0

    # area
    current_area = [min_x, min_y]
    area = 0
    n_rows = max_x - min_x + 1

    for _, _, hex_s in ins:

        hex_s = hex_s[2:-1]
        length = int(hex_s[:5], base=16)
        direction = hex_s[-1]

        move = dirs[direction]
        action = (length, move)

        # perimeter
        for i in range(length):
            current = current[0] + move[0], current[1] + move[1]
            perimeter.add(current)

            min_x = min(min_x, current[0])
            min_y = min(min_y, current[1])
            max_x = max(max_x, current[0])
            max_y = max(max_y, current[1])

        mx, my = move[0] * length, move[1] * length

        area += (n_rows - current_area[0]) * my
        current_area[0] += mx
        current_area[1] += my

        print(f"action: {action} area: {area}")

    units_perimeter = len(perimeter)
    solution = area + units_perimeter // 2 + 1

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
