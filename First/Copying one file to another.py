#  Here an image is copied

img1 = open("Wilfred.jpg", 'rb')

img2 = open("Wilfred_Copy.jpg", 'wb')

for i in img1:
    img2.write(i)

print("Copy Successfull")