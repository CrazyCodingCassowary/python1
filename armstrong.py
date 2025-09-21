# take input from thhe user
num = int(input("Enter a number"))

#initialize sum
sum = 0

# find the sum of the cube of each digit
t = num
while t>0:
    d = t%10
    sum += d
    t //=10

#display the result
if num == sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")