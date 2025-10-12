#take input
print("half pyramid pattern of stars(*): ")
n = int(input("enter the number of rows: "))
#outer loop to handle number of rows
for i in range(n):
    #inner loop to handle number of columns
    for j in range(i+1):
        #display result
         print("*", end="")
    print()


num = int(input("Enter the number of rows: "))
numb = 1

print("Floyd's Triangle")
for i in range(1, num + 1):
     for j in range(1, i+1):
           print(numb, end = " ")
           numb = numb +1
     print( )



rs = int(input("enter the number of rows"))
if rs%2==0:
     hd = int(rs/2)
else:
      hd = int(rs/2)+1
s = hd-1
for i in range(1, hd+1):
     for j in range (1, s+1):
          print(end = " ")
     s = s-1
     num = 1
     for j in range(2*i-1):
          print(end = str (num))
          num =num+1
     print()
s = 1
for i in range(1, hd):
     for j in range(1, s+1):
          print(end=" ")
     s = s+1
     num = 1
     for j in range(1, 2*(hd-i)):
          print(end=str(num))
          num = num+1
     print()