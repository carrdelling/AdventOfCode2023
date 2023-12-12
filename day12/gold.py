from collections import Counter
from functools import lru_cache


@lru_cache(maxsize=None)
def count_posibilities(pattern, placed, springs):

    # the string is empty
    if len(pattern) < 1:
        if len(springs) == 0 and placed == 0:
            return 1
        if len(springs) == 1 and placed == springs[0]:
            return 1
        return 0

    # no more springs to place
    if placed > 0 and len(springs) == 0:
        return 0

    # not enough space to place all springs
    symbols = Counter(pattern)
    spring_spaces = symbols['#'] + symbols['?']

    if spring_spaces + placed < sum(springs):
        return 0

    # job done
    if len(springs) < 1:
        if symbols['#'] == 0 and placed < 1:
            return 1
        else:
            return 0

    # need to close a run and cannot finish
    if pattern[0] == '.' and placed not in {springs[0], 0}:
        return 0

    pos = 0

    if placed > 0:

        # continue
        if pattern[0] == '.':
            pos += count_posibilities(pattern[1:], 0, springs[1:])

        # add a spring
        if pattern[0] in {'#', '?'}:
            pos += count_posibilities(pattern[1:], placed + 1, springs)

        # don't add a spring for now
        if pattern[0] == '?' and placed == springs[0]:
            pos += count_posibilities(pattern[1:], 0, springs[1:])

    else:
        # put the first spring
        if pattern[0] in {'#', '?'}:
            pos += count_posibilities(pattern[1:], 1, springs)

        # don't add a spring for now
        if pattern[0] in {'.', '?'}:
            pos += count_posibilities(pattern[1:], 0, springs)

    return pos


def solve(data):
    arrangements = 0

    for row in data:
        pattern, counts = row.split()

        counts = tuple(map(int, counts.split(',')))

        # expand the string
        exp_pattern = '?'.join([pattern] * 5)
        counts *= 5

        pos = count_posibilities(exp_pattern, 0, counts)

        arrangements += pos

    solution = arrangements

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
