# of 'is' identity operator
x = 5
if (type(x)is int):
    print("True")
else:
    print("False")



x = 5.0
if (type(x)is not float):
    print("True")
else:
    print("False")


x = 20
y = 20

if (x is y):
    print("x and y SAME identity")

y = 30

if (x is y):
    print("x and y DIFFERENT identity")


a = 10
b = -10

# print bitwise right shift operator
print("a >> 1=",a >> 1)
print("b >> 1 =",b >> 1)

a = 5
b = -10

# print bitwise left shift operator
print("a << 1=",a << 1)
print("b << 1 =",b << 1)

print("Enter points obtained in 5 subjects:")
one = int(input())
two = int(input())
three = int(input())
four = int(input())
five = int(input())


tot = one+two+three+four+five
avg = tot/5

if avg >= 91 and avg <= 100:
    print("Your  grade is A1")
elif avg >= 81 and avg < 91:
    print("your grade is A2")
elif avg >= 71 and avg < 81:
    print("your grade is B1")
elif avg >= 61 and avg < 71:
    print("your grade is B2")
elif avg >= 51 and avg < 61:
    print("your grade is C1")
elif avg >= 41 and avg < 51:
    print("your grade is C2")
elif avg >= 33 and avg < 41:
    print("your grade is D1")
elif avg >= 21 and avg < 33:
    print("your grade is D2")
else:
    print("invalid input!!!")