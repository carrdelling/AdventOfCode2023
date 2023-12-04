

def solve(data):

    points = 0

    for row in data:
        w, mine = row.split(':')[-1].strip().split('|')
        w_n = {int(k.strip()) for k in w.split() if len(k) > 0}
        mine_n = {int(k.strip()) for k in mine.split() if len(k) > 0}

        match = len(w_n) - len(w_n - mine_n)

        score = 2 ** (match - 1) if match > 0 else 0
        points += score

    solution = points

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
