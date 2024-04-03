def validate_type(prompt, type_needed):
    while True:
        try:
            value = type_needed(input(prompt + ": "))
            return value
        except (TypeError, ValueError):
            print("Invalid Input, Try Again.")


def valid_range(number, min_value, max_value):
    if max_value >= number >= min_value:
        return True
    else:
        return False
