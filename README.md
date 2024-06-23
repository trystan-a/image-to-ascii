# Image to ASCII Converter

This Image to ASCII Converter takes an image and will convert it into a text file representation
using the Pillow library

## Installation

To install the program, download the file "imageToASCII.py" from the github page:
https://github.com/trystan-a/image-to-ascii

You will also need to have Python and the Pillow library installed to run the file

## Usage

To use this file you will first need to have an image that you would want to
convert into a text representation. Make sure you have the image inside the same folder as
the python file.

To run the file, open your terminal of your choice (Command prompt is recommended), and navigate
to the file that cotains your image and python file using a series of "cd" commands.

Once you are at the correct file, run the command "python imageToASCII.py" in the terminal.

This will prompt you to input two things, the name of the file and the extension. The name is simple, just enter whatever your image file is called. The extension refers to the type of image
file it is, whether it be a png, jpg, bmp, etc. Input that file extension (without the .)

After you give the image name and extension, the program will begin converting, as shown by the
progress shown in the terminal. Once the program is finished, a markdown (.md) file will be added
to the folder with the python file and image file that will contain the text representation

Example using the image file testImage.jpg:

python imageToASCII.py
Enter your filename (Without the extension): testImage
Enter the extension (Example: png, jpg): jpg

## Todo List (Ordered from most important -> least important)

1.) Improve the classifyColour function to either include more colours or refactor the
    whole function

2.) Fix bug that prevents files that arent .jpg files from working

3.) Refer to pixels in square groups of pixels to make the final text representation smaller,
    adding support for bigger images