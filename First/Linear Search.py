n = int(input("Enter item to Search\n"))
s = None
list = [3, 2, 6, 3, 5]
for i in list:
    if i == n:
        s = i

if (s == n):
    print(n, ' Found at ', list.index(i) + 1)
else:
    print("Not Found")
