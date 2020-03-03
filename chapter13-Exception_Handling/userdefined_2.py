class Error(Exception):
    pass
class TosmallError(Error):
    pass
class TolargeError(Error):
    pass

no=10
number=int(input("Enter Number: "))
try:
    if number>no:
        raise TolargeError
    elif number<no:
        raise  TosmallError
    else:
        print("Guess the right number!!!!!")
except TosmallError:
    print("Guess number is small....")
except TolargeError:
    print("Guess number is large...")
