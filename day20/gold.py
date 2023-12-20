from copy import deepcopy
from collections import deque
from math import lcm


def pulse(first_signal, machines, states, target):

    signals = deque([(n, False, 'broadcaster') for n in first_signal])

    output = None
    while len(signals) > 0:
        m, high_pulse, sender = signals.popleft()
        t, outputs, inputs = machines[m]

        if t == '%':
            if high_pulse:
                continue
            # xor, flip-flop
            states[m] = states[m] != bool(True)
            # print(f"{m} flip flop goes to {states[m]}")
            for o in outputs:
                # print(f"Sends {states[m]} to {o}")
                signals.append((o, states[m], m))
            continue
        if t == '&':
            states[m][sender] = high_pulse

            # print(f"{m} combiner updates {sender} => {states[m]}")
            combined = not all(states[m].values())
            # print(f"{m} combiner total: {combined}")
            # shortcircuit
            if m == target and combined:
                return True, None, None

            for o in outputs:
                # print(f"Sends {combined} to {o}")
                signals.append((o, combined, m))
            continue

        if t == 'problem_output':
            output = high_pulse
            continue
        assert False

    return False, states, output


def simulate(first_signal, machines, initial_states):

    targets = ['xj', 'qs', 'kz', 'km']
    cycles = []
    for target in targets:

        states = deepcopy(initial_states)
        shortcircuit = False
        pulses = 1

        while not shortcircuit:
            shortcircuit, states, output = pulse(first_signal, machines, states, target)
            pulses += 1

        cycles.append(pulses-1)

    solution = lcm(*cycles)

    return solution


def solve(data):
    first_signal = None
    machines = {'rx': ['problem_output', [], []], 'output': ['problem_output', [], []]}
    states = {}
    for row in data:
        component, outputs = row.split(' -> ')
        outputs = outputs.split(', ')

        if component == 'broadcaster':
            first_signal = outputs
        else:
            t, name = component[0], component[1:]
            machines[name] = [t, outputs, []]

            if t == '%':
                states[name] = False
            if t == '&':
                states[name] = {}

    for n, (t, outputs, inputs) in machines.items():
        for o in outputs:
            if machines[o][0] == '&':
                machines[o][-1].append(n)
                states[o][n] = False

    solution = simulate(first_signal, machines, states)

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
