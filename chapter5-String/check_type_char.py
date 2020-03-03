s=input("Enter String: ")

if(s.isalnum()):
    print("It's AlphaNumeric...")
    if(s.isalpha()):
        print("All are Alphabets...")
        if(s.islower()):
            print("All r lower case..")
        else:
            print("All r Upper case..")
    else:
        print("It's Digit...")
elif(s.isspace()):
    print("It's space....")
else:
    print("It's Special Character...")