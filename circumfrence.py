import math

def calculate_circumference(radius):
 
  if radius < 0:
    raise ValueError("Radius cannot be negative.")
  circumference = 2 * math.pi * radius
  return circumference


radius1 = 5
circumference1 = calculate_circumference(radius1)
print(f"The circumference of a circle with radius {radius1} is: {circumference1}")

radius2 = 10.5
circumference2 = calculate_circumference(radius2)
print(f"The circumference of a circle with radius {radius2} is: {circumference2}")

