from collections import defaultdict


def distances(point, neighbour, adj):

    dist = 1
    a, b = point, neighbour

    while len(adj[b]) == 2:
        dist += 1
        c = [x for x in adj[b] if x != a][0]
        a = b
        b = c

    return b, dist


def solve(data):
    field = []

    for i, row in enumerate(data):
        new_row = list(x.replace('^', '.').replace('v', '.').replace('>', '.').replace('<', '.') for x in row)
        field.append(new_row)

    # full adjacency matrix
    adj = defaultdict(list)
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == '#':
                continue
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < len(field):
                    if 0 <= ny < len(field[0]):
                        if field[nx][ny] != '#':
                            adj[(i, j)].append((nx, ny))

    new_adj = defaultdict(list)
    for i in range(len(field)):
        for j in range(len(field[0])):
            point = i, j

            for neigh in adj[point]:
                new_adj[point].append(distances(point, neigh, adj))

    # new_adj[p] = [(n, steps)]
    start = 0, 1
    goal = 140, 139

    max_steps = 0
    visited = frozenset([start])
    start_state = (0, start, visited)

    states = [start_state]

    print("start search")
    while states:
        steps, loc, fvisisted = states.pop()

        if loc == goal:
            if steps > max_steps:
                max_steps = steps
                print(f"Best so far: {max_steps}")
            continue

        visited = set(fvisisted)

        for new_loc, cost in new_adj[loc]:
            if new_loc not in visited:
                new_steps = steps + cost
                new_visited = visited.copy()
                new_visited.add(new_loc)

                new_state = (new_steps, new_loc, frozenset(new_visited))
                states.append(new_state)

    solution = max_steps

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
