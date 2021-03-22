#  File handling is done using some methods


f = open('myfile.txt', 'w')

f.write("Wilfred Almeida, Hello")
f.close()

f1 = open('myfile.txt', 'r')
print(f1.readline())
f1.close()