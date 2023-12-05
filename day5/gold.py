

def extend_options(options, mappings):

    mapped = []
    live_options = list(options)

    for raw_map in mappings:
        # ranges are [a, b) here too
        s = raw_map[1]
        e = raw_map[1] + raw_map[2]
        delta = raw_map[0] - raw_map[1]

        passed_options = []
        for option in live_options:

            left = (option[0], min(option[1], s))
            inside = (max(option[0], s), min(e, option[1]))
            right = (max(e, option[0]), option[1])

            if left[1] > left[0]:
                passed_options.append(left)
            if inside[1] > inside[0]:
                mapped.append((inside[0] + delta, inside[1] + delta))
            if right[1] > right[0]:
                passed_options.append(right)
        else:
            live_options = list(passed_options)

    output = sorted(mapped + live_options)

    return output


def solve(data):

    parsing = parse_input(data)
    seeds = parsing[0]
    raw_mappings = parsing[1:]

    # ranges are [a, b)
    seed_ranges = [(a, a+d) for a, d in list(zip(seeds[::2], seeds[1::2]))]

    for idx, raw_mapping in enumerate(raw_mappings):
        seed_ranges = extend_options(seed_ranges, raw_mapping)

    solution = min(seed_ranges[0])

    return solution


def parse_input(data):

    idx = 0
    seeds = list(map(int, data[idx].split()[1:]))
    idx = 3
    seed_soil_raw = []

    while len(data[idx]) > 2:
        d, s, r = list(map(int, data[idx].split()))
        seed_soil_raw.append((d, s, r))
        idx += 1
    idx += 2
    soil_fertilizer_raw = []
    while len(data[idx]) > 2:
        d, s, r = list(map(int, data[idx].split()))
        soil_fertilizer_raw.append((d, s, r))
        idx += 1
    idx += 2
    fertilizer_water_raw = []
    while len(data[idx]) > 2:
        d, s, r = list(map(int, data[idx].split()))
        fertilizer_water_raw.append((d, s, r))
        idx += 1
    idx += 2
    water_light_raw = []
    while len(data[idx]) > 2:
        d, s, r = list(map(int, data[idx].split()))
        water_light_raw.append((d, s, r))
        idx += 1
    idx += 2
    light_temperature_raw = []
    while len(data[idx]) > 2:
        d, s, r = list(map(int, data[idx].split()))
        light_temperature_raw.append((d, s, r))
        idx += 1
    idx += 2
    temperature_humidity_raw = []
    while len(data[idx]) > 2:
        d, s, r = list(map(int, data[idx].split()))
        temperature_humidity_raw.append((d, s, r))
        idx += 1
    idx += 2
    humidity_location_raw = []
    while len(data[idx]) > 2 and idx < len(data) - 1:
        d, s, r = list(map(int, data[idx].split()))
        humidity_location_raw.append((d, s, r))
        idx += 1
    d, s, r = list(map(int, data[idx].split()))
    humidity_location_raw.append((d, s, r))

    return seeds, seed_soil_raw, soil_fertilizer_raw, fertilizer_water_raw, water_light_raw, \
           light_temperature_raw, temperature_humidity_raw, humidity_location_raw


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
