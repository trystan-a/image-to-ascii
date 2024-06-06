from PIL import Image

filename = input("Enter your filename (Without the extension): ")
extension = input("Enter the extension (Example: png, jpg): ")

imageFile = filename + "." + extension
textFile = filename + ".md"

image = Image.open(imageFile)
width, height = image.size

file = open(textFile, "w")

for x in range(width):
    for y in range(height):
        r, g, b = image.getpixel((x, y))


