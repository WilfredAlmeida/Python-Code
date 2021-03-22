# s = "mom"
# l1 = []
# for i in s:
#     l1.append(i)
# l1.reverse()
#
# s2 = ""
#
# for j in l1:
#     s2 += j
#
# if s == s2:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

s="mom"
if s==s[-1::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")