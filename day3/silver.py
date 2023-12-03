from itertools import product


def moves(x):

    for i, j in product([-1, 0, 1], repeat=2):
        yield x[0] + i, x[1] + j


def solve(data):

    max_x = len(data)
    parts = 0

    for x, line in enumerate(data):
        max_y = len(line)
        n = 0
        symbol = False

        # for every char in the line
        for y, c in enumerate(line):

            # accumulate digits
            if c.isdigit():
                n = n * 10 + int(c)

                # search for symbols
                for i, j in moves((x, y)):
                    if 0 <= i < max_x:
                        if 0 <= j < max_y:
                            is_not_symbol = (data[i][j] == '.') or data[i][j].isdigit()
                            if not is_not_symbol:
                                symbol = True
                                break

            # process full number
            if not c.isdigit():
                if symbol:
                    parts += n
                    symbol = False
                n = 0
        else:
            # number at the end of the line
            if symbol:
                parts += n

    solution = parts

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
