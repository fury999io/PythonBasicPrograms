#To check whether a number is perfect or plaindrome or not

def Perfect(num):
    a=1
    sum=0
    while(a<num):
        if num%a==0:
            sum=sum+a
        a=a+1
    if sum==num:
        return "The number is perfect"
    else:
        return "The number is not perfect"

def Palindrome(num):
    rev=""
    while(num>0):
        rev=rev+str(num%10)
        num=num/10
    if rev==str(n):
        return "The number is palindrome"
    else:
        return "The number is not palindrome"

print("Enter a number")
n=int(input())

print("Enter 1 for perfect number, 2 for palindrome number")
inp=int(input())

if inp==1:
    print(Perfect(n))
else:
    print(Palindrome(n))
