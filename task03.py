#1
for i in range(5,0,-1):
  for j in range(i,0,-1):
    print(j,end="")
  print("")

#2
for i in range(1,6):
  for col in range(1, i+1 ):
    print("*",end=" ")
  for sp in range(5,i,-1):
    print(" ",end=" ")
  print( )
  
#3
for i in range(4,0,-1):
  for col in range(1,i+1):
    print("*",end=" ")
  for sp in range(5, i ,-1):
    print(" ",end=" ")
  print( )

#4
for i in range(1,4):
  for j in range(2,0):
    print("i",end=" ")
  for col in range(1,5):
    print("*",end=" ")
    
#5
n=4
for i in range(1, n):
    print(" " * (n - i) + "*"*(2 * i - 1))

#6
for i in range(1,6):
  print(end="\n")
  for j in range(i,0,-1):
    print(j,end=" ")
print( )

#7
n = int (input("enter the number"))
for i in range(0,n):
  x = "x^{}/{}".format(i,i)
  print(x,end="+")

#8
x=int(input("Enter a number"))
sum= 0
for i in range(1,8):
  term = (x**i)/i
  sum += term
  print(sum)

#9
n=int(input("number:"))
term=0
sum=0
for i in range(1,n+1):
  term=term*10+2
  sum+=term
  print(term,end="+")
if i != n:
  print("",end="")
print("")
print("sum of above series is:",sum,)

#10
for i in range(1,5):
  for j in range(1,5):
     print(j,k,end=" ")
for k in range (1,5):
  print(end=" ")
print("")

