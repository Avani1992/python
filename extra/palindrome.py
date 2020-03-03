class palindrome:
    def palindrome(self):
        s=input("Enter String:").strip() # avoid space...
        s1=s[::-1]
        if(s==s1):
            print(s+" is Palindrome String...")
        else:
            print(s + " is not Palindrome String...")

p1=palindrome()
p1.palindrome()