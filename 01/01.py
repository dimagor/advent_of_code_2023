import re


def extract_numbers(txt):
    nums = re.findall(r"\d", txt)
    return nums


def extract_words_and_numbers(txt):
    sub_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    all_nums = re.findall("(?=(one|two|three|four|five|six|seven|eight|nine|\d))", txt)

    nums = [sub_dict.get(n, n) for n in all_nums]

    return nums


def get_digit(nums):
    digit = int(nums[0] + nums[-1])
    return digit


def get_digit_from_numbers(txt):
    return get_digit(extract_numbers(txt))


def get_digit_from_words_and_numbers(txt):
    return get_digit(extract_words_and_numbers(txt))


if __name__ == "__main__":
    input = "01/input"
    with open(input) as f:
        lines = f.read().splitlines()

    # Part 1
    p1_digits = [get_digit_from_numbers(l) for l in lines]
    print(f"The answer to 1.1 is: {sum(p1_digits)}")

    # Part 2
    p2_digits = [get_digit_from_words_and_numbers(l) for l in lines]
    print(f"The answer to 1.2 is: {sum(p2_digits)}")
