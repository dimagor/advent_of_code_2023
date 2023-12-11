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


if __name__ == "__main__":
    input = "03/input"
    with open(input) as f:
        lines = f.read().splitlines()

    part_numbers = get_valid_part_numbers(lines)
    print(f"The answer to 3.1 is: {sum(part_numbers)}")
