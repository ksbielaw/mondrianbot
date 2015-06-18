# for Image
import Image, ImageDraw
import random
import os

# for Twitter
import tweepy
import glob
import random

# for botting and playing well together
import time

# to pretend like I can keep my data hidden
import secrets

auth = tweepy.OAuthHandler(secrets.api_key,secrets.api_secret)
auth.set_access_token(secrets.oauth_token, secrets.oauth_token_secret)
api = tweepy.API(auth)

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def randomimagetwitt(imagename):
	# images = glob.glob(imagename)
	# print images
	# image_open = images[0]
	api.update_with_media(imagename)

#######################################################################
### Mondrian Image Maker Section
### Very Similar to Javascript version I made on jsfiddle
#######################################################################

# Define the colors for this project
colors = ["#FF0000","#0000FF","#FFFF00","#FFFFFF","#FFFFFF"]

# newImage draws and saves an image with the appropriate filename
def newImage(filename) :
	im = Image.new("RGB",(500,500),"white")
	draw = ImageDraw.Draw(im)
	hlines = [0]
	vlines = [0]	
	# make a set number of horizontal and vertical vertices
	hVerts = random.randint(1,9) # number of horizontal lines
	vVerts = random.randint(1,9) # number of vertical lines
	hlines = makeLines(hVerts,0,draw) #draws the lines
	vlines = makeLines(vVerts,1,draw) #draws vertical lines
	vertices = findVerts(hlines,vlines,draw) # finds and stores vertices
	drawRectangles(hlines,vlines,vertices,draw) # draws rectanges
	draw.line((0,0,0,500),fill='#FFFFFF',width=1)
	draw.line((0,0,500,0),fill='#FFFFFF',width=1)
	draw.line((500,0,500,500),fill='#FFFFFF',width=1)
	draw.line((0,500,500,500),fill='#FFFFFF',width=1)
	del draw
	im.save(filename, "JPEG")


def makeLines(verts,dir,draw1):
	# dir == 0 if horizontal, 1 if vertical
	lines = [0]
	for i in range(0,verts):
		position = random.randint(1,499)
		if dir == 0:
			draw1.line( (0,position,500,position), fill = '#000000',width=1)
			lines.append(position)
		if dir == 1:
			draw1.line( (position,0,position,500), fill = '#000000',width=1)
			lines.append(position)
	lines.append(500)
	lines.sort()
	return lines

def findVerts(hlines,vlines,draw1):
	vertices = []
	for i in range(0,len(vlines)):
		for j in range(0,len(hlines)):
			vertices.append([vlines[i],hlines[j]])

	return vertices

def drawRectangles(hlines,vlines,vertices,draw1):
	i = 0
	while i < len(hlines)-1 :
		j = 0
		while j < len(vlines)-1 :
			try: 
				tempcoord = vertices.index([vlines[j],hlines[i]])
				mycoord = [vlines[j],hlines[i]]
				numh = min(random.randint(1,3),len(hlines)-i)
				numv = min(random.randint(1,3),len(vlines)-j)
				nextcoord = [vlines[numv+j-1],hlines[numh+i-1]]
				myColor = colors[random.randint(0,4)]
				draw1.rectangle(((mycoord[0],mycoord[1]),(nextcoord[0],nextcoord[1])),fill = myColor,outline = "#000000")
				# Remove the reminaing squares
				for p in range(j,numv+j-1):
					for q in range(i,numh+i-1):
						tempcoord = vertices.index([vlines[p],hlines[q]])
						vertices.pop(tempcoord)
			except ValueError:
				a = 'a' 
			j = j+1
		i = i+1

alpha = 0
while 1==1:
	filename = 'm' + str(alpha) + '.jpg'
	newImage(filename)
	time.sleep(5)
	randomimagetwitt(filename)
	time.sleep(21595)
