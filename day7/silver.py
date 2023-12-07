from collections import Counter


def translate(hand):

    replacements = {'T': 'a', 'J': 'b', 'Q': 'c', 'K': 'd', 'A': 'e'}

    return ''.join(replacements.get(x, x) for x in hand)


def solve(data):

    bids = {}

    by_type = [[] for _ in range(7)]

    for row in data:
        cards, score = row.split()
        scards = translate(cards)
        bids[scards] = int(score)

    for hand in bids:

        reps = Counter(hand)
        best_2 = reps.most_common(2)

        if max(reps.values()) == 5:
            by_type[6].append(hand)
            continue
        if max(reps.values()) == 4:
            by_type[5].append(hand)
            continue
        if max(reps.values()) == 3:
            if best_2[-1][-1] == 2:
                by_type[4].append(hand)
            else:
                by_type[3].append(hand)
            continue
        if max(reps.values()) == 2:
            if best_2[-1][-1] == 2:
                by_type[2].append(hand)
            else:
                by_type[1].append(hand)
            continue

        assert len(reps) == 5
        by_type[0].append(hand)

    winnings = 0
    scored = 0

    for hand_type in range(7):
        hands = sorted(by_type[hand_type])[::1]
        for option in hands:
            score = bids[option] * (scored+1)
            winnings += score
            scored += 1

    solution = winnings

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
