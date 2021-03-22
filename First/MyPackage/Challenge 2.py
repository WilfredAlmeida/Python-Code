
# --------------Start: Additive Persistence----------------------
num = int(input("Enter number: "))

s = str(num)

num_list = list(s)

sum_of_list = 0

for i in num_list:
    sum_of_list += int(i)


s1 = str(sum_of_list)

num_list2 = list(s1)

additive_persistence = 0

for i in num_list2:
    additive_persistence += int(i)

print(sum_of_list,"\n",additive_persistence)

# --------------End: Additive Persistence----------------------

# --------------Start: Multiplicative Persistence----------------------

s = str(num)

num_list = list(s)

sum_of_list = 1

for i in num_list:
    sum_of_list *= int(i)


s1 = str(sum_of_list)

num_list2 = list(s1)

multiplicative_persistence = 1

for i in num_list2:
    multiplicative_persistence *= int(i)

print(sum_of_list,"\n",multiplicative_persistence)

# --------------End: Multiplicative Persistence----------------------
