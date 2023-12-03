from collections import defaultdict


def parse(data):
    cases = {}
    for game in data:
        _id, contents = game.split(':')
        _id = int(_id.split()[-1])
        contents = [x.strip().split(', ') for x in contents.split(';')]

        cases[_id] = contents

    return cases


def solve(data):
    games = parse(data)

    solution = 0
    for _id, game in games.items():
        seen = defaultdict(int)
        for show in game:

            for color in show:
                n, c = color.split()
                seen[c] = max(seen[c], int(n))

        power = seen['red'] * seen['green'] * seen['blue']
        solution += power

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
