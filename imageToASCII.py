from PIL import Image

# Credit to Jacob Ritchie for the classifyColours function
# https://stackoverflow.com/questions/36439384/classifying-rgb-values-in-python
def classifyColours(r, g, b):
    rgbTuple = (r, g, b)

    colours = {"black": (0, 0, 0),
               "grey": (128, 128, 128),
               "white": (255, 255, 255),
               "red": (255, 0, 0),
               "green": (0, 255, 0),
               "blue": (0, 0, 255),
               "yellow": (255, 255, 0),
               "magenta": (255, 0, 255),
               "cyan": (0, 255, 255)}
    
    manhattanDistance = lambda x,y: abs(x[0] - y[0]) + abs(x[1] - y[1]) + abs(x[2] - y[2])
    distances = {k: manhattanDistance(v, rgbTuple) for k, v in colours.items()}
    colour = min(distances, key = distances.get)
    return colour

counter = 0

filename = input("Enter your filename (Without the extension): ")
extension = input("Enter the extension (Example: png, jpg): ")

imageFile = filename + "." + extension
textFile = filename + ".md"

image = Image.open(imageFile)
width, height = image.size

pixelCount = width * height

file = open(textFile, "w")

for y in range(height):
    for x in range(width):
        r, g, b = image.getpixel((x, y))
        if(classifyColours(r, g, b) == "black"):
            file.write("#")
        if(classifyColours(r, g, b) == "grey"):
            file.write("0")
        if(classifyColours(r, g, b) == "white"):
            file.write("I")
        if(classifyColours(r, g, b) == "red"):
            file.write("@")
        if(classifyColours(r, g, b) == "green"):
            file.write("X")
        if(classifyColours(r, g, b) == "blue"):
            file.write("%")
        if(classifyColours(r, g, b) == "yellow"):
            file.write("&")
        if(classifyColours(r, g, b) == "magenta"):
            file.write("!")
        if(classifyColours(r, g, b) == "cyan"):
            file.write("$")
        
        counter += 1
        print("Progress: " + str(counter) + "/" + str(pixelCount) + " pixels")
    file.write("\n")

print("Conversion complete!")

file.close()