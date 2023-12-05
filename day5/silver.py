

def map_dict(v, rules):

    for row in rules:
        start = row[1]
        c = row[2]
        t_start = row[0]
        if start <= v <= (start + c):
            return t_start + (v - start)

    return v


def solve(data):

    parsing = parse_input(data)
    seeds = parsing[0]
    raw_mappings = parsing[1:]

    min_v = 9E99
    for s in seeds:

        current = s
        for rm in raw_mappings:
            current = map_dict(current, rm)

        min_v = min(min_v, current)

    solution = min_v

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

    return seeds, seed_soil_raw, soil_fertilizer_raw, fertilizer_water_raw, water_light_raw,\
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


