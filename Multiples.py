print("Enter the divisor") 
div = float(input())

indicator=0

nums=[]
print("Enter 5 numbers")
count=0
while(count<5):
    x = float(input())
    nums.append(x)
    count=count+1

count2=0
print("The multiples of", div, "are")
while(count2<5):
    if(nums[count2]%div==0):
        print(nums[count2])
        indicator=1
    count2=count2+1

if(indicator==0):
    print("No multiples found")