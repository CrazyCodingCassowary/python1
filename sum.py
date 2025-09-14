#input an integer value
n = int (input("Enter the number whose sum you want to find"))
sum = 0

#Iterates for n+1 times : i = 1 to n = 1
for i in range (1,n+1):
    sum = sum+i
    print("\n Sum = ",sum)


#Input a word or sentence
s = input("Please enter a string: ")

s2 = ('')
# loop for printing in reverse
for i in s:
    s2 = i + s2

print("\n The original string = ",s)
print("The reversed string = ", s2)

# input number greater than 1
n = int(input("Enter the value of n: "))

#print the numbers from n to 1
print("numbers from {0} to {1} are: ".format(n,1))

#loop to print numbers
for i in range(n,0,-1):
    print(i)