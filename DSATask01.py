#1.
L=[1,2,3,4,5]
sum=0
for i in L:
    sum=sum+1
print(sum)
product=1
for i in L:
    product=product*i
print(product)

#2
for i in L:
  for j in L:
    print("{},{}".format(i,j))
    
#3.
def intostr(i):
  digit="0123456789"
  if i==0:
    return "0"
  result=" "
  while i>0:
    result=digit[i%10]+result
    i=i//10
  return result

#Q5
L=[1,2,3,4,5]
for i in range(len(L)):
  for j in range(i+1,len(L)):
    print("{},{}".format(i,j))

#Q6
A=[1,2,3,4]
B=[2,3,4,5,6]
for i in A:
  for j in B:
    if i<j:
      print("{}.{}".format(i,j))
      
#Q7
A=[1,2,3,4]
B=[2,3,4,5]
for i in A:
  for j in B:
    for k in range(1):
      print("{},{}".format(i,j))
      
#Q8
def factorial(n):
  if n==1:
    return 1
  else:
    return n*factorial(n-1)

#Q9
def fib(n):
  if n==1 or n==0:
    return 1
  else:
    return fib(n-1)+fib(n-2)