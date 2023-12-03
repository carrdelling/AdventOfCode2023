from collections import defaultdict
from itertools import product


def moves(x):

    for i, j in product([-1, 0, 1], repeat=2):
        yield x[0] + i, x[1] + j


def solve(data):

    gears = defaultdict(list)
    max_x = len(data)

    for x, line in enumerate(data):
        max_y = len(line)
        n = 0
        gear = None

        # for every char in the line
        for y, c in enumerate(line):

            # accumulate digits
            if c.isdigit():
                n = n * 10 + int(c)

                # search for gears
                for i, j in moves((x, y)):
                    if 0 <= i < max_x:
                        if 0 <= j < max_y:
                            if data[i][j] == '*':
                                gear = (i, j)
                                break   # looks like it works assuming only a single gear

            # process full number
            if not c.isdigit():
                if gear is not None:
                    gears[gear].append(n)
                    gear = None
                n = 0
        else:
            # number at the end of the line
            if gear is not None:
                gears[gear].append(n)

    solution = sum(numbers[0] * numbers[1] for numbers in gears.values() if len(numbers) == 2)

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
