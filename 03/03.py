import re


def get_valid_part_numbers(lines):
    part_numbers = []
    for idx, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            left_bound = max(match.start() - 1, 0)
            right_bound = min(match.end() + 1, len(line) - 1)
            top_bound = max(idx - 1, 0)
            bottom_bound = min(idx + 1, len(lines) - 1)
            search_space = (
                lines[top_bound][left_bound:right_bound]
                + lines[idx][left_bound:right_bound]
                + lines[bottom_bound][left_bound:right_bound]
            )
            if re.search(r"[^0-9A-Za-z.]", search_space):
                part_numbers.append(int(match.group(0)))
    return part_numbers


def find_connected_parts(line, gear_position):
    connected_parts = []
    for part in re.finditer(r"\d+", line):
        part_span = list(range(part.start(), part.end()))
        if (
            gear_position - 1 in part_span
            or gear_position + 1 in part_span
            or gear_position in part_span
        ):
            connected_parts.append(int(part.group(0)))
    return connected_parts


def calc_gear_ratios(lines):
    gear_ratios = []
    for idx, line in enumerate(lines):
        for match in re.finditer(r"\*", line):
            connected_parts = []
            gear_position = match.start()
            connected_parts += find_connected_parts(lines[idx], gear_position)
            if idx > 0:
                connected_parts += find_connected_parts(lines[idx - 1], gear_position)
            if idx + 1 < len(lines):
                connected_parts += find_connected_parts(lines[idx + 1], gear_position)
            if len(connected_parts) == 2:
                gr = connected_parts[0] * connected_parts[1]
                gear_ratios.append(gr)
    return gear_ratios


if __name__ == "__main__":
    input = "03/input"
    with open(input) as f:
        lines = f.read().splitlines()

    part_numbers = get_valid_part_numbers(lines)
    print(f"The answer to 3.1 is: {sum(part_numbers)}")

    gear_ratios = calc_gear_ratios(lines)
    print(f"The answer to 3.2 is: {sum(gear_ratios)}")
