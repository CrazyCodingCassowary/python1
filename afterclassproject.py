def decimal_to_binary_recursive(n):
    if n > 1:
        decimal_to_binary_recursive(n // 2)
    print(n % 2, end='')

decimal_number = 25
decimal_to_binary_recursive(decimal_number)
print() # For a new line after the binary output