from collections import deque


def solve(data):

    guide = list(data[0].strip())

    paths = {}
    for row in data:
        if '=' in row:
            t, d = row.strip().split(' = ')
            dl, dr = d[1:-1].split(', ')
            paths[t] = (dl, dr)

    initial = (0, 'AAA', 0)
    states = deque([initial])

    # made a mistake, though this was a search problem (!)
    while True:

        current = states.popleft()
        cost, loc, turn = current
        print(current)
        if loc == 'ZZZ':
            solution = cost
            break

        if turn >= len(guide):
            turn = 0
        r_or_l = 0 if guide[turn] == 'L' else 1

        next_loc = paths[loc][r_or_l]
        cost += 1
        turn += 1

        next_state = (cost, next_loc, turn)
        states.append(next_state)

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
