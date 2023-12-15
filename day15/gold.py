
def hashing(code):

    current = 0

    for c in code:
        current += ord(c)
        current = (current * 17) % 256

    return current


def solve(data):

    codes = [c for c in data[0].split(',')]

    hashmap = {i: [] for i in range(256)}
    hashmap_values = {}
    for code in codes:

        if code[-1] == '-':
            label = code[:-1]

            if label not in hashmap_values:
                continue
            del hashmap_values[label]

            cell = hashing(label)
            hashmap[cell].remove(label)

        else:
            label, value = code.split('=')

            # note position of the new key
            if label not in hashmap_values:
                cell = hashing(label)
                hashmap[cell].append(label)

            hashmap_values[label] = int(value)

    solution = 0
    for box, contents in hashmap.items():
        box_value = box + 1

        for slot, key in enumerate(contents, 1):
            value = hashmap_values[key]
            power = box_value * slot * value
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
