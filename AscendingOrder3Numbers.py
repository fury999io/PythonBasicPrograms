print("Input the first number")
num1=int(input())
print("Input the second number")
num2=int(input())
print("Input the third number")
num3=int(input())

print("The numbers in ascending order are: ", end=" ")

if num1>num2 and num1>num3:
    print(num1, end=", ", sep=", ")
    if num2>num3:
        print(num2, num3, sep=", ")
    else:
        print(num3, num2, sep=", ")
elif num2>num3:
    print(num2, end=", ", sep=", ")
    if num3>num1:
        print(num3, num1, sep=", ")
else:
    print(num3, num2, num1, sep=", ")
    