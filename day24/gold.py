from scipy.optimize import fsolve


def solve(data):

    points = []
    for row in data:
        pos, speed = [tuple(map(int, c.split(', '))) for c in row.split(' @ ')]
        points.append((pos, speed))

    candidates = [points[5], points[25], points[125]]  # any triplet of points should be enough

    def intersection(p):

        x, y, z, dx, dy, dz = p

        all_eqs = []
        for point in candidates:
            ((x1, y1, z1), (xv1, yv1, zv1)) = point

            equation_a = (x - x1) * (dy - yv1) - (y - y1) * (dx - xv1)
            equation_b = (x - x1) * (dz - zv1) - (z - z1) * (dx - xv1)

            all_eqs += [equation_a, equation_b]

        return all_eqs

    partial_solution = fsolve(intersection, points[0][0] + points[0][1])

    solution = round(partial_solution[0] + partial_solution[1] + partial_solution[2])

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
