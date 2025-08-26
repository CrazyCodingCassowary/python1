v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;
print("Value of(v+w) * x/ y is ", z)

name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else :
    print("Goodbye!!")


print("Enter a number (Numerator): ")
numn = int(input())
print("Enter a number (denominator): ")
numd = int(input())

if numn%numd == 0:
    print("\n" +str(numn)+" is divisible by " +str(numd))
else :
    print("\n" +str(numn)+" is not divisible by " +str(numd))


mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40

#sum of 40 nmbers

sum = mean1*total_number
print("The sum of 40 numbers: ",sum)

#correct sum of these numbers

num2 = sum-(wrong_number-correct_number)
print("sum-((wrong_number)-(correct number)): ",num2)

#the correct mean
mean2 = num2/total_number
print(mean2)


a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))
c = int(input("Enter value 3: "))

avg = (a + b +c)/3
print("avg = ",avg)

if avg > a and avg > b and avg > c :
    print("%d is higher than %d, %d, %d" %(avg, a, b, c))

elif avg > a and avg > b:
    print("%d is higher than %d, %d" %(avg, a, b))
elif avg > a and avg > c :
    print("%d is higher than %d, %d" %(avg, a, c))
elif  avg > b and avg > c :
    print("%d is higher than %d, %d" %(avg, b, c))
elif avg > a:
    print("%d is higher than %d" %(avg, a))
elif avg > b :
    print("%d is higher than %d" %(avg, b))
elif  avg > c :
    print("%d is higher than %d" %(avg, c))
else:
    print("invalid input")
