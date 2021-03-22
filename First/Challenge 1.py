# Question: WAP which will take one string as input and tell
# number of letters required to make it palindrome.
# Question from Instagram -> nextgencoder

s = str(input("Enter a string: \n"))

s2 = str()

l = list(s)
l2 = list(s)

l.reverse()

if l == l2:
    print("Already Palindrome")
else:
    s2 += s[-2::-1]
    s += s2

    print(s)
    print("Number of letters required to make string palindrome are: ", len(s2))
