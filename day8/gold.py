from math import lcm


def solve(data):
    guide = list(data[0].strip())

    paths = {}
    for row in data:
        if '=' in row:
            t, d = row.strip().split(' = ')
            dl, dr = d[1:-1].split(', ')
            paths[t] = (dl, dr)

    current_states = []
    for l in paths:
        if l[-1] == 'A':
            current_states.append(l)

    turn = 0
    cost = 0

    final_cost = set()
    while len(current_states) > 0:

        new_states = []
        r_or_l = 0 if guide[turn] == 'L' else 1

        for current in current_states:
            loc = current

            if loc[-1] == 'Z':
                final_cost.add(cost)
            else:
                next_loc = paths[loc][r_or_l]
                new_states.append(next_loc)
        else:
            cost += 1
            turn += 1
            current_states = list(new_states)
            if turn >= len(guide):
                turn = 0

    solution = lcm(*final_cost)

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
