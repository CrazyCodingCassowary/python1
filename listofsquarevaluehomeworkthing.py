start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

s = []
e_s = []
o_s = []

for i in range(start, end + 1):
    sq = i * i
    s.append(sq)

    if sq % 2 == 0:
        e_s.append(sq)
    else:
        o_s.append(sq)

print("Square values:", s)
print("Even square values:", e_s)
print("Odd square values:", o_s)