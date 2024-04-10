def get_valid_type(prompt, type_needed):
    while True:
        try:
            value = type_needed(input(prompt + ": "))
            return value
        except (TypeError, ValueError):
            print("Invalid Input, Try Again.")


def get_valid_range(prompt, min_value, max_value):
    number = get_valid_type(prompt, int)
    while not (max_value >= number >= min_value):
        prompt_invalid = f"Invalid Range, Must be between {min_value} & {max_value}"
        number = get_valid_type(prompt_invalid, int)
    return number

# Use Case:
# if __name__ == '__main__':
#     hello = get_valid_range("Give me your numbers", 1, 10)