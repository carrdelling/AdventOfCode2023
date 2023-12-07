from collections import Counter


def translate(hand):

    replacements = {'T': 'a', 'J': '0', 'Q': 'c', 'K': 'd', 'A': 'e'}

    return ''.join(replacements.get(x, x) for x in hand)


def score_hand(hand):

    reps = Counter(hand)
    best_2 = reps.most_common(2)

    if max(reps.values()) == 5:
        return 6
    if max(reps.values()) == 4:
        return 5
    if max(reps.values()) == 3:
        if best_2[-1][-1] == 2:
            return 4
        else:
            return 3
    if max(reps.values()) == 2:
        if best_2[-1][-1] == 2:
            return 2
        else:
            return 1

    return 0


def solve(data):

    bids = {}

    by_type = [[] for _ in range(7)]

    for row in data:
        cards, score = row.split()
        scards = translate(cards)
        bids[scards] = int(score)

    for hand in bids:
        best = -1
        best_hand = ''
        for option in "edca98765432":
            new_hand = hand.replace('0', option)
            opt_type = score_hand(new_hand)

            if opt_type > best:
                best = opt_type
                best_hand = hand
            elif opt_type == best:
                best_hand = max(best_hand, hand)

        by_type[best].append(hand)

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
