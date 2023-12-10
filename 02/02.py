import re


def extract_draws(draws_str):
    draws_split = draws_str.split(";")

    draw_list = []

    for g in draws_split:
        draw_info = {}
        for draw in g.split(","):
            draw_split = draw.strip().split(" ")
            color = draw_split[1]
            count = draw_split[0]
            draw_info[color] = int(count)
        draw_list.append(draw_info)
    return draw_list


def build_games_dict(lines):
    games = {}

    for l in lines:
        name_split = l.split(":")
        game_number = int(re.findall("\d+$", name_split[0])[0])
        draw_str = name_split[1]
        games[game_number] = extract_draws(draw_str)
    return games


def is_valid_game(draws_list, rules):
    for d in draws_list:
        for color in d.keys():
            if d[color] > rules[color]:
                return False
    return True


def find_valid_games(games, rules):
    invalid_ids = []
    for game_id, draws_list in games.items():
        if is_valid_game(draws_list, rules):
            invalid_ids.append(game_id)
    return invalid_ids


# TODO: Bit hacky with hardcoding, revisit.
def get_power(draws_list):
    max_vals = {
        color: max(d.get(color, 1) for d in draws_list)
        for color in ["red", "blue", "green"]
    }

    power = 1
    for v in max_vals.values():
        power *= v
    return power


if __name__ == "__main__":
    input = "02/input"
    with open(input) as f:
        lines = f.read().splitlines()

    games = build_games_dict(lines)

    rules = {"red": 12, "green": 13, "blue": 14}
    invalid_ids = find_valid_games(games, rules)
    print(f"The answer to 2.1 is: {sum(invalid_ids)}")

    powers = [get_power(d) for d in games.values()]
    print(f"The answer to 2.2 is: {sum(powers)}")
