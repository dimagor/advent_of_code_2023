import re


def scratch_point_total(lines):
    point_total = 0
    for l in lines:
        card_split = l.split(":")
        card_number = re.findall(r"\d+", card_split[0])[0]
        game_split = card_split[1].split("|")
        scratch_numbers = {
            int(i.strip()) for i in game_split[0].strip().split(" ") if i.strip() != ""
        }
        winning_numbers = {
            int(i.strip()) for i in game_split[1].strip().split(" ") if i.strip() != ""
        }
        n_matches = len(scratch_numbers.intersection(winning_numbers))
        points = max(0, int(2 ** (n_matches - 1)))
        point_total += points
    return point_total


if __name__ == "__main__":
    input = "04/input"
    with open(input) as f:
        lines = f.read().splitlines()

    print(f"Part 4.1: {scratch_point_total(lines)}")
