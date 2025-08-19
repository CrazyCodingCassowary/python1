a = 10
b = 12
c = 10

if a and b and c:
    print("All the numbers have a boolean value as true")
else:
    print("At least one number has boolean  value as false")

a = 10
b = -10
c = 0

if a > 0 or b > 0:
    print(" Either number is greater than 0")
else:
    print("No number is greater than 0")

if b > 0 or c > 0:
    print(" Either number is greater than 0")
else:
    print("No number is greater than 0")


a = 10
b = 12
c = 12

a = "python"
b = "coding"

if a != b :
    print(a,'and', b,'are different')

a = 4
b = 5

if (a==1) != (b==5):
    print('Hello')


a = int(input("Enter a number"))

if a%2 !=0:
    print(a,"is not an even number")


height = float(input("enter your height "))
weight = float(input("enter your  weight "))

BMI = weight / (height/100)**2
print("your BMI is",  BMI)

if BMI<= 18.4:
    print("you are underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <= 29.9:
    print("you are overweight")
elif BMI <= 34.9:
    print("you are severly overweight")
elif BMI <= 39.9:
    print("you are you are obese")
else:
    print("you are severly obese")