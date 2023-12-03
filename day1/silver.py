
def solve(data):

    solution = 0

    for s in data:
        d = [x for x in s if x.isdigit()]
        solution += (10*int(d[0])) + int(d[-1])

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
