
def hashing(code):

    current = 0

    for c in code:
        current += ord(c)
        current = (current * 17) % 256

    return current


def solve(data):

    codes = [c for c in data[0].split(',')]

    solution = sum(hashing(c) for c in codes)

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
