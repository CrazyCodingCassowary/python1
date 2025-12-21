import math


s = 90

# Convert degrees to radians for the math module functions
angle_radians = math.radians(s)

# Calculate sine, cosine, and tangent
sine_value = math.sin(angle_radians)
cosine_value = math.cos(angle_radians)
tangent_value = math.tan(angle_radians)

# Print the results (for 90 degrees, sine is 1, cosine is ~0, tangent is undefined/very large)
print(f"The sine of {s} degrees is: {sine_value}")
print(f"The cosine of {s} degrees is: {cosine_value}")
print(f"The tangent of {s} degrees is: {tangent_value}")
