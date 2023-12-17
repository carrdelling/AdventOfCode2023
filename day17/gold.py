import heapq

MAX_MOVE = 10
MIN_MOVE = 4


def moves(node, lava):

    pos, dir, vel = node
    x, y = pos
    dx, dy = dir

    front = x + dx, y + dy
    if vel < MAX_MOVE and front in lava:
        yield (front, dir, vel + 1,), lava[front]

    if vel >= MIN_MOVE:
        left = x - dy, y + dx
        if left in lava:
            yield (left, (-dy, dx), 1), lava[left]

        right = x + dy, y - dx
        if right in lava:
            yield (right, (dy, -dx), 1), lava[right]


def solve(data):

    lava = {}
    max_x, max_y = 0, 0
    for x, row in enumerate(data):
        max_x = max(max_x, x)
        for y, c in enumerate(row):
            lava[x, y] = int(c)
            max_y = max(max_y, y)

    seen = set()

    go_down = ((0, 0), (1, 0), 0)
    go_right = ((0, 0), (0, 1), 0)

    states = [(0, go_down), (0, go_right)]
    best_cost = {go_down: 0, go_right: 0}

    while states:
        cost, current = heapq.heappop(states)

        if current in seen:
            continue
        seen.add(current)

        for move, cost in moves(current, lava):
            if move in seen:
                continue

            new_cost = best_cost.get(current) + cost
            if new_cost < best_cost.get(move, 1E9):
                best_cost[move] = new_cost
                heapq.heappush(states, (new_cost, move))

    solution = 1E9
    target = max_x, max_y
    for k, cost in best_cost.items():
        if k[0] == target:
            solution = min(solution, cost)

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
