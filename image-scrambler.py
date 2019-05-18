import urllib.request
import urllib.parse
import urllib.error
import urllib.response
import cv2 #pip3 install python-opencv
import numpy #pip3 install numpy
import os, sys
import math

rowspace = 0
colspace = 0
# python image-scrambler.py <file> <divide> <row px> <col px>
if(len(sys.argv)>5):
	print("Invalid arguments passed. Try with --help")
if(sys.argv[1] == ("--help" or "-h")):
	print("""Usage: python image-scrambler.py <file> <divide> <row px> <col px> \nTransposes the given image which can be a url. Can be used on itself to revert back the effects.\nSaves the transposed image to the folder the script is running in with [filename](transposed).fileextension \n\nExample: python image-scrambler.py image-location.jpg 4""")
if(len(sys.argv)==5):
	rowspace = sys.argv[4]
	colspace= sys.argv[5]
if(len(sys.argv)<6):
	if(len(sys.argv)==2):
		sys.argv.append(4)
	if(sys.argv[1].find("http")!= -1):
		findbeg = sys.argv[1].rfind('/')
		finddotbeg = sys.argv[1].find(".",findbeg)
		if(finddotbeg != -1):
			filename = sys.argv[1][findbeg+1:finddotbeg]
			fileexten = sys.argv[1][finddotbeg+1:]
			readarr = numpy.asarray(bytearray(urllib.request.urlopen(sys.argv[1]).read()), dtype=numpy.uint8)
		else:
			filename = sys.argv[1][findbeg+1:finddotbeg]
			print("No file extension found. Using png.")
			fileexten = "png"

	else:
		filename = sys.argv[1][:sys.argv[1].find(".")]
		fileexten = sys.argv[1][sys.argv[1].find(".")+1:]
		readarr = numpy.asarray(bytearray(open(sys.argv[1],'rb').read()), dtype=numpy.uint8)
	img = cv2.imdecode(readarr,-1)
	areas = []
	b= 4*(math.floor(len(img[0]) / 32) *8) - colspace
	a= 4*(math.floor(len(img)/ 32) *8) - rowspace
	sys.argv[2] = int(sys.argv[2])
	for i in range(sys.argv[2]*sys.argv[2]):
		row = (i // sys.argv[2]) + 1
		col = (i % sys.argv[2]) + 1
		start1 = (row-1)*(a//sys.argv[2])
		end1 = row*(a//sys.argv[2])
		start2 = (col-1)*(b//sys.argv[2])
		end2 = col*(b//sys.argv[2])
		t = img[start1: end1, start2:end2]
		areas.append(t)
		areas2 = []
	for i in range(sys.argv[2]):
		for j in range(i, i+sys.argv[2]*sys.argv[2]-sys.argv[2]+1, sys.argv[2]):
			areas2.append(areas[j])
	img2 = img.copy()
	for i in range(sys.argv[2]*sys.argv[2]):
		row = (i // sys.argv[2]) + 1
		col = (i % sys.argv[2]) + 1
		start1 = (row-1)*(a//sys.argv[2])
		end1 = row*(a//sys.argv[2])
		start2 = (col-1)*(b//sys.argv[2])
		end2 = col*(b//sys.argv[2])
		img2[start1: end1, start2:end2] = areas2[i]
	cv2.imwrite(filename+"(transposed)."+fileexten,img2)