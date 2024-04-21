def get_valid_type(prompt, type_needed):
    while True:
        try:
            value = type_needed(input(prompt + ": "))
            return value
        except (TypeError, ValueError):
            print("Invalid Input, Try Again.")


def get_valid_range(prompt, min_value=1, max_value=31):
    # 31 is default as it's the largest amount of data that can go on one filed
    number = get_valid_type(prompt, int)
    while not (max_value >= number >= min_value):
        prompt_invalid = f"Invalid Range, Must be between {min_value} & {max_value} : "
        number = get_valid_type(prompt_invalid, int)
    return number


def get_valid_string(prompt, min_len, max_len):
    given_string = input(prompt)
    while not (min_len <= len(given_string) <= max_len):
        prompt_invalid = f"Input Must be between {min_len} & {max_len} Characters : "
        given_string = input(prompt_invalid)
    return given_string

# Use Case:
# if __name__ == '__main__':
#     hello = get_valid_range("Give me your numbers", 1, 10)
