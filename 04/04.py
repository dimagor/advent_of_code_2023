import re


def calc_points(n_matches):
    return max(0, int(2 ** (n_matches - 1)))


def scratch_matches(lines):
    match_values = []
    for l in lines:
        card_split = l.split(":")
        game_split = card_split[1].split("|")
        scratch_numbers = {
            int(i.strip()) for i in game_split[0].strip().split(" ") if i.strip() != ""
        }
        winning_numbers = {
            int(i.strip()) for i in game_split[1].strip().split(" ") if i.strip() != ""
        }
        n_matches = len(scratch_numbers.intersection(winning_numbers))
        match_values.append(n_matches)
    return match_values


def calc_card_counts(matches):
    cards = {c: {"count": 1, "matches": m} for c, m in enumerate(matches)}

    for k, v in cards.items():
        c = v.get("count")
        m = v.get("matches")
        for i in range(k + 1, k + m + 1):
            cards[i]["count"] += c

    total_cards = sum([v.get("count") for v in cards.values()])
    return total_cards


if __name__ == "__main__":
    input = "04/input"
    with open(input) as f:
        lines = f.read().splitlines()

    matches = scratch_matches(lines)
    points = [calc_points(m) for m in matches]
    print(f"Part 4.1: {sum(points)}")

    print(f"Part 4.1: {calc_card_counts(matches)}")
