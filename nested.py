#Take input of a word
s = input("Enter your own word: ")
#Take input of a character
c = input("Enter your own character: ")
i = 0
count = 0
#loop will to find the occurence of character
while(i < len(s)): #string operation

    if (s[i] == c): #condition 1
        count = count + 1
    i = i+1

#display result
print("The total number of times ", c, "has appeared = ",count)

#take two input from user
l = int(input("Enter an lower range: "))
u = int(input("Enter a upper range: "))

print("Prime numbers between ",l," and ", u,"are : ")
#iterate loop from lower limit to upper limit
for num in range(l,u+1):
    #all prime numbers are greater than 1
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break

        else:
            print(num)

#input a number
num = int(input("Enter a number : "))
t = num
numLen  = 0
#iterate the loop
while t>0:
    numLen = numLen+1
    t = int(t/10)

if numLen >= 4: #condition 1
    numLen = int(numLen/2)
    chk = 0
    while num>0: #iterate loop
        rem = num%10
        if chk==numLen: #nested condition 1
            midOne = rem
        elif chk==(numLen-1):
            midTwo = rem
        num = int(num/10)
        chk = chk+1
    prod = midOne*midTwo #product of middle digits
    #display the result
    print("\nProduct of mid digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ", prod)

else:
    print("\nIt's not a 4 or more digit number !!!")