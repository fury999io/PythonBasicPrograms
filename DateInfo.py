print("Input today's date(1-31) ...", end=" ")
dat=int(input())
print("Input the month in digits(1-12) ...", end=" ")
mont=int(input())

if mont==2:
    dleft=28-dat
elif mont%2==0:
    dleft=30-dat
else:
    dleft=31-dat

print()

print("The month has", str(dleft), "days remaining")
