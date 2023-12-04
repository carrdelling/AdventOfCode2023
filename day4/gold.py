
def solve(data):

    points = {}

    for idx, row in enumerate(data):
        w, mine = row.split(':')[-1].strip().split('|')
        w_n = {int(k.strip()) for k in w.split() if len(k) > 0}
        mine_n = {int(k.strip()) for k in mine.split() if len(k) > 0}

        match = len(w_n) - len(w_n - mine_n)

        points[idx] = match

    # sim
    cards = {i+1: 1 for i in range(len(data))}
    for i in range(1, max(points)+1):

        copies = cards[i]
        l = points[i-1]

        for j in range(1, l + 1):
            idx = i+j
            if idx <= max(cards):
                cards[idx] += copies

    solution = sum(cards.values())

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
