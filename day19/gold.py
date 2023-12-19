
def parse_input(data):

    rules = {}

    parsing_rules = True
    pieces = []
    for row in data:

        if parsing_rules:
            if len(row) < 2:
                parsing_rules = False
                continue

            tag, body = row[:-1].split('{')
            clauses = []
            for case in body.split(','):
                if case == "R":
                    clauses.append(False)
                    continue
                if case == "A":
                    clauses.append(True)
                    continue
                if ":" not in case:
                    clauses.append(case)
                    continue
                test, target = case.split(":")
                clauses.append((test, target))
            rules[tag] = clauses
        else:
            p = tuple(int(chunk.split('=')[-1]) for chunk in row[1:-1].split(','))
            pieces.append(p)

    return rules, pieces


def evaluate(rule, x, m, a, s):

    for clause in rule:
        if isinstance(clause, bool):
            return clause
        if '<' in clause[0] or '>' in clause[0]:
            if eval(clause[0]):
                if clause[1] == 'R':
                    return False
                if clause[1] == 'A':
                    return True
                return clause[1]
        else:
            return clause


def reduce_intervals(variable_idx, is_gt, threshold, intervals):

    valid_intervals = []

    for interval in intervals:
        a, b = interval[variable_idx]

        if is_gt:
            a = max(a, threshold + 1)
        else:
            b = min(b, threshold - 1)
        if a > b:
            # this interval is False ==> we lose it
            continue

        interval[variable_idx] = (a, b)
        valid_intervals.append(interval)

    return valid_intervals


def evaluate_ranges(clauses, rules):

    current_clause = clauses[0]

    # last clause is a bool
    if isinstance(current_clause, bool):
        if current_clause:
            return [[(1, 4000), (1, 4000), (1, 4000), (1, 4000)]]
        else:
            return []

    # last clause is (almost) a bool
    if current_clause == 'A':
        return [[(1, 4000), (1, 4000), (1, 4000), (1, 4000)]]
    elif current_clause == 'R':
        return []

    # last clause is a full rule
    if not ('<' in current_clause[0] or '>' in current_clause[0]):
        return evaluate_ranges(rules[current_clause], rules)

    variable_idx = {c: i for i, c in enumerate('xmas')}[current_clause[0][0]]

    is_gt = '>' in current_clause[0]
    threshold = int(current_clause[0][2:])
    reverse_gt = not is_gt
    rev_threshold = threshold + 1 if is_gt else threshold - 1

    true_intervals = reduce_intervals(variable_idx, is_gt, threshold, evaluate_ranges([current_clause[1]], rules))
    false_intervals = reduce_intervals(variable_idx, reverse_gt, rev_threshold, evaluate_ranges(clauses[1:], rules))

    all_intervals = true_intervals + false_intervals

    return all_intervals


def solve(data):

    rules, cases = parse_input(data)

    output_ranges = evaluate_ranges(rules['in'], rules)

    solution = 0
    for branch in output_ranges:
        pos = 1
        for a, b in branch:
            pos *= b - a + 1
        solution += pos

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
