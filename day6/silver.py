
def solve(data):

    times = {i: int(t) for i, t in enumerate(data[0].split(':')[-1].split())}
    records = {i: int(t) for i, t in enumerate(data[1].split(':')[-1].split())}

    races = len(times)

    solution = 1
    for race in range(races):

        t = times[race]
        target = records[race]
        wins = 0

        for h in range(t+1):
            dist = h * (t-h)
            if dist > target:
                wins += 1

        print(wins)
        solution *= wins

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
