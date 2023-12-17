from images import Image
image1 = Image("smokey.gif")
#image1.draw()

image = Image(150, 150)

blue = (255, 255, 0)
y = image.getHeight() // 2
for x in range(image.getWidth()):
    image.setPixel(x, y - 1, blue)
    image.setPixel(x, y, blue)
    image.setPixel(x, y + 1, blue)
image.draw()