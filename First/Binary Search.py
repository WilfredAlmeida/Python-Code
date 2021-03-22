while True:
    n = int(input("Enter Number to search:\n"))
    list = [1,2,3,4,5,6,7,8,9]

    first = list[0]
    last = list[len(list)-1]
    mid = first // last

    s = None
    index = None
    for i in list:
        if n == i:
            s = i
            index = list.index(i)
        else:
            if mid <= n:
                mid = i+1
            else:
                mid = i-1

    if s == n:
        print(n, ' Found at position', index + 1)
    else:
        print("Not Found")
