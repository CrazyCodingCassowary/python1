# input base and exponent
b = float(input("Enter the number: "))
e = int(input("Enter the power"))

# initialize result
r = 1

# multiply base, exponent times
for i in range(e):
    r = r*b

print(f"{b} raised to the power {e} is: {r}")