#image-scrambler

Basic transposing of an image.

#Dependecies

open-cv (pip3 install python-opencv)
numpy (pip3 install numpy)

#Usage

python image-scrambler.py <file> <divide> <row px> <col px>

Supply it with a path to a file (can be a url) that can be read from and number to divide the picture into and optionally some space to leave it untouched.
Currently divides the image to 4x4 and can leave extra spaces to be left untouched.
