def validate_type(prompt, type_needed):
    while True:
        try:
            value = type_needed(input(prompt + ": "))
            return value
        except (TypeError, ValueError):
            print("Invalid Input, Try Again.")


def validate_range(number, min_value, max_value):
    if max_value >= number >= min_value:
        return number
    else:
        return validate_range(validate_type("Invalid Range, Try Again", int), min_value, max_value)
