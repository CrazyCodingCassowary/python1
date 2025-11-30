def check_integer_and_parity(input_string):
    """
    Checks if a given string is an integer and determines if it's odd or even.

    Args:
        input_string: The string to be checked.

    Returns:
        A string describing whether the input is an integer and its parity,
        or a message indicating it's not an integer.
    """
    try:
        number = int(input_string)
        if number % 2 == 0:
            return f"'{input_string}' is an even integer."
        else:
            return f"'{input_string}' is an odd integer."
    except ValueError:
        return f"'{input_string}' is not a valid integer."

# Example usage:
user_input = input("Enter a string: ")
result = check_integer_and_parity(user_input)
print(result)

user_input_2 = "123"
result_2 = check_integer_and_parity(user_input_2)
print(result_2)

user_input_3 = "-4"
result_3 = check_integer_and_parity(user_input_3)
print(result_3)

user_input_4 = "hello"
result_4 = check_integer_and_parity(user_input_4)
print(result_4)

user_input_5 = "3.14"
result_5 = check_integer_and_parity(user_input_5)
print(result_5)
