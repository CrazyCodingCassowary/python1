# using a try and exept
try:
    num = int(input("Enter a number: "))
    print("The number entered is", num)

#using value error
except ValueError as ex:
    print("Exeption: ",ex)

