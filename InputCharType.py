print("Enter a character")
ch=input()

if len(ch)>1:
    print("Please input one character only")
    exit()

if str(ch)>="0" and str(ch)<="9":
    print("The character is a digit")
elif str(ch)>="A" and str(ch)<="Z":
    print("This is an uppercase character")
elif str(ch)>="a" and str(ch)<="z":
    print("This is a lowercase character")
else:
    print("This is a special character")