

def solve(data):

    series = [tuple(map(int, row.strip().split())) for row in data]

    extra_history = 0
    for s in series:
        intermediate = [s]
        while len(set(s)) > 1:
            t = tuple([b-a for a, b in zip(s, s[1:])])
            intermediate.append(t)
            s = t

        extra = 0
        for t in intermediate[::-1]:
            extra = t[-1] + extra
        else:
            extra_history += extra

    solution = extra_history

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


