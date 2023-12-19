

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


def solve(data):

    rules, cases = parse_input(data)

    solution = 0
    for x, m, a, s in cases:
        output = evaluate(rules['in'], x, m, a, s)

        while output not in [True, False]:
            output = evaluate(rules[output], x, m, a, s)

        if output:
            solution += x + m + a + s

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
