#Program to check whether an entered number is a vowel, consonant, digit or special character

print("Enter a character")
ch=input()

if len(ch)>1:
    print("Enter a single character only")
    exit()

if ch>='a' and ch<='z' or ch>='A' and ch<='Z':
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
        print("The entered character is a vowel")
    else:
        print("The entered character is a consonant")

elif ch>='0' and ch<='9':
    print("The entered character is a digit")

else:
    print("The entered character is a special character")
