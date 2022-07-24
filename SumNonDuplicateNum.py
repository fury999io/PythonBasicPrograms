lst = []
x=0
y=0
sum=0

print("How many numbers would you like to add?")
n = int(input())

print("Input ", n, " numbers")
while x<n:
   num=int(input())
   lst.append(num)
   x=x+1

indicator=0

x=0
while x<n:
   while y<x:
      indicator=0
      if lst[y]==lst[x]:
         indicator=1
      y=y+1
   if indicator==0:
      sum=sum+lst[x]
   x=x+1

print("The sum of the numbers excluding duplicates: ", sum)