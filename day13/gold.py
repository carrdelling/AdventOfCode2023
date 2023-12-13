

def parse(data):

    buffer = []

    for row in data:
        if len(row) < 2:
            yield buffer
            buffer = []
            continue

        buffer.append(row)

    if len(buffer) > 1:
        yield buffer


def find_mirrors(problem, factor):

    score = 0

    for jj in range(1, len(problem[0])):
        mistakes = 1
        is_mirror = True
        for row in problem:
            if not is_mirror:
                continue
            mirror_row = zip(row[jj - 1::-1], row[jj::])
            for x, xx in mirror_row:
                if x != xx and mistakes == 1:
                    mistakes = 0
                    continue
                if x != xx and mistakes == 0:
                    is_mirror = False
                    break
        if is_mirror and mistakes == 0:
            score += (jj * factor)
    return score


def solve(data):

    solution = 0
    for problem in parse(data):

        # y axis - mirrors score 1
        solution += find_mirrors(problem, 1)

        # x axis - mirrors score 100
        problem_t = list(map(list, zip(*problem)))
        solution += find_mirrors(problem_t, 100)

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
