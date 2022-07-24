 
print("Input the radius of the circle")
rad = float(input())

choice=int(input("Enter 1 for calculating area and 2 for calculating perimeter... "))

if choice==1:
    area=22/7*rad*rad
    print("Area of the circle: ", area)
elif choice==2:
    perimeter=2*22/7*rad
    print("Perimeter of the circle: ", perimeter)
else:
    print("Invalid choice")

