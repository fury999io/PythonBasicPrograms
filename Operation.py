 
print("Input the first operand")
num1=eval(input())
print("Enter the second operand")
num2=eval(input())
print("Enter the operator")
opr=input()
res=0
print("The result of the operation is: ", end=" ")
if opr=="+":
    print(num1+num1)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("Invalid operator")