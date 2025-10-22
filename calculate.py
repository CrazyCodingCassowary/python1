def add(P,Q):
    return P + Q
def subtract(P,Q):
    return P - Q
def multiply(P,Q):
    return P * Q
def divide(P,Q):
    return P / Q

print("select the operation")
print("a. addition")
print("b. substract")
print("c. multiply")
print("d. divide")



choice = input("enter your choice (a,b,c,d): ")

num1 = int(input("please enter your first number: "))
num2 = int(input("please enter your second number: "))

if choice == "a":
    print(num1," + ",num2," = ",add(num1,num2))
elif choice == "b":
    print(num1," - ",num2," = ",subtract(num1,num2))
elif choice == "c":
    print(num1," * ",num2," = ",multiply(num1,num2))
elif choice == "d":
    print(num1," / ",num2," = ",divide(num1,num2))
else:
    print("this is an invalid input")
