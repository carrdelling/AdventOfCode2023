from itertools import product


def horizontal_points(piece):
    start, end = piece

    if start[0] != end[0]:
        return [(i, start[1]) for i in range(start[0], end[0] + 1)], False
    elif start[1] != end[1]:
        return [(start[0], i) for i in range(start[1], end[1] + 1)], False
    else:
        return (start[0], start[1]), True


def solve(data):
    pieces = []
    for row in data:
        start, end = row.split('~')

        # the input pieces are sorted - for all coords, left <= right
        for i in [0, 1, 2]:
            assert start[i] <= end[i]

        pieces.append((list(map(int, start.split(','))), list(map(int, end.split(',')))))

    # sort by z ascending - min_z => left
    pieces = sorted(pieces, key=lambda x: x[0][2])
    height = {(i, j): 0 for i, j in product(range(10), repeat=2)}
    top = {(i, j): (-1, 0) for i, j in product(range(10), repeat=2)}  # p, h
    dependences = {}

    # throw all the pieces down, one by one
    for idx, p in enumerate(pieces):
        points, is_vertical = horizontal_points(p)
        if is_vertical:
            base, current_h = top[points]
            h = (p[1][2] - p[0][2]) + 1
            height[points] += h
            top[points] = idx, height[points]

            if base != -1:
                dependences[idx] = [base]
        else:
            max_h = max(height[point] for point in points)
            new_h = max_h + 1

            base_pieces = set()
            for point in points:
                base, current_h = top[point]
                if base != -1 and current_h == max_h:
                    base_pieces.add(base)
                height[point] = new_h
                top[point] = idx, new_h

            dependences[idx] = sorted(base_pieces)

    solution = 0
    # see what happens if we take out each piece
    for to_break in range(len(pieces)):
        broken = {to_break}

        added = True
        while added:
            added = False
            for idx, dep in dependences.items():
                if idx in broken:
                    continue
                # if it has dependences and all dependences are broken, the piece falls
                if len(dep) > 0:
                    if all(d in broken for d in dep):
                        broken.add(idx)
                        added = True

        solution += len(broken) - 1

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
