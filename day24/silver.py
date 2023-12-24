from itertools import combinations


def intersection(a, b):

    (ax, ay, az), (sx, sy, sz) = a
    (bx, by, bz), (tx, ty, tz) = b

    d = sx * ty - sy * tx

    if d == 0:
        return None

    t = ((bx - ax) * ty - (by - ay) * tx) / d
    u = ((bx - ax) * sy - (by - ay) * sx) / d

    tx = ax + t * sx
    ty = ay + t * sy

    return tx, ty, t, u


def solve(data):

    points = []
    for row in data:
        pos, speed = [tuple(map(int, c.split(', '))) for c in row.split(' @ ')]
        points.append((pos, speed))

    valid = 0
    for a, b in combinations(points, 2):

        i_point = intersection(a, b)

        if i_point is None:
            continue
        x, y, t, u = i_point

        if (
                (200000000000000 <= x <= 400000000000000) and
                (200000000000000 <= y <= 400000000000000) and
                (t > 0) and (u > 0)
        ):
            valid += 1

    solution = valid

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
