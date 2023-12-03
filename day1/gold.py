
NUMBERS = {s: i for i, s in enumerate([
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine']
)}

def solve(data):

    solution = 0

    for s in data:
        r = 0
        for idx in range(len(s)):
            if r > 0:
                break

            if s[idx].isdigit():
                r += int(s[idx]) * 10

            for n in NUMBERS:
                if s[idx:].startswith(n):
                    r += NUMBERS[n] * 10

        for idx in range(len(s) - 1, -1, -1):
            if r % 10 > 0:
                break

            if s[idx].isdigit():
                r += int(s[idx])

            for n in NUMBERS:
                if s[:idx+1].endswith(n):
                    r += NUMBERS[n]

        solution += r

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
