def print_mirrored_right_triangle(rows, char='*'):
   
    for i in range(1, rows + 1):
        
        print(" " * (rows - i), end="")
        
        print(char * i)

num_rows = int(input("Enter the number of rows for the triangle: "))
pattern_char = input("Enter the character to use (e.g., *, #, $): ")


print_mirrored_right_triangle(num_rows, pattern_char)
