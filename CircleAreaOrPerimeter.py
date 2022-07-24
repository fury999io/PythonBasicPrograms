print("To calculate area, enter 1")
print("To calculate area, enter 2")
choice=int(input())

print("Enter the radius of the circle")
r = float(input())

if(choice==1):
    print("The area of the circle is", (22/7*r*r))
else:
    print("The perimeter of the circle is", (2*22/7*r))