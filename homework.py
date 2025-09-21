n = int(input("Enter a number :"))
c = 0
while n>0:
    n=n//10
    c = c+1
    print("number of digits: ", c)
