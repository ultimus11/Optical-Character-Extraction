import cv2
import numpy as np
def get_grid_array(gray_image,grid_height,grid_width):
	grid_1 = []
	grid_2 = []
	grid_3 = []
	grid_4 = []
	grid_5 = []
	grid_6 = []
	grid_7 = []
	grid_8 = []
	grid_9 = []
	xposition=0
	yposition=0
	for y in gray_image:
		xposition=0
		gridx1=[]
		gridx2=[]
		gridx3=[]
		gridx4=[]
		gridx5=[]
		gridx6=[]
		gridx7=[]
		gridx8=[]
		gridx9=[]
		for x in y:
			#here we get every element of grid in one list
			#first row
			#first grid
			if xposition<=grid_width and yposition<=grid_height:
				#grid_1.append([x])
				gridx1.append(x)
			#second grid
			if xposition<=grid_width*2 and xposition>=grid_width and yposition<=grid_height:
				gridx2.append(x)
			#third grid
			if xposition<=grid_width*3 and xposition>=grid_width*2 and yposition<=grid_height:
				gridx3.append(x)
			#second row
			#4th grid
			if xposition<=grid_width and yposition<=grid_height*2 and yposition>=grid_height:
				gridx4.append(x)
			#5th grid
			if xposition<=grid_width*2 and xposition>=grid_width and yposition<=grid_height*2 and yposition>=grid_height:
				gridx5.append(x)
			#6th grid
			if xposition<=grid_width*3 and xposition>=grid_width*2 and yposition<=grid_height*2 and yposition>=grid_height:
				gridx6.append(x)
			#third row
			#7th grid
			if xposition<=grid_width and yposition<=grid_height*3 and yposition>=grid_height*2:
				gridx7.append(x)
			#8th grid
			if xposition<=grid_width*2 and xposition>=grid_width and yposition<=grid_height*3 and yposition>=grid_height*2:
				gridx8.append(x)
			#9th grid
			if xposition<=grid_width*3 and xposition>=grid_width*2 and yposition<=grid_height*3 and yposition>=grid_height*2:
				gridx9.append(x)
			xposition+=1
		if gridx1:
			grid_1.append(gridx1)
		if gridx2:
			grid_2.append(gridx2)
		if gridx3:
			grid_3.append(gridx3)
		if gridx4:
			grid_4.append(gridx4)
		if gridx5:
			grid_5.append(gridx5)
		if gridx6:
			grid_6.append(gridx6)
		if gridx7:
			grid_7.append(gridx7)
		if gridx8:
			grid_8.append(gridx8)
		if gridx9:
			grid_9.append(gridx9)
		yposition+=1

	return grid_1,grid_2,grid_3,grid_4,grid_5,grid_6,grid_7,grid_8,grid_9
def line_detection(grid):
	xposition=0
	yposition=0
	black_pixels=[]
	for y in grid:
		xposition=0
		for x in y:
			if x==0:
				#note that xposition is first element
				black_pixels.append([xposition,yposition])
			xposition+=1
		yposition+=1
	print(black_pixels)
	x_counter={}
	y_counter={}
	firsttime=0
	for x in black_pixels:
		y=x[1]
		x=x[0]
		if firsttime==0:
			x_counter[x]=1
			y_counter[y]=1
			firsttime=1
		elif firsttime!=0:
			if x in x_counter:
				x_counter[x]=x_counter[x]+1
			else:
				x_counter[x]=1
			if y in y_counter:
				y_counter[y]=y_counter[y]+1
			else:
				y_counter[y]=1
		print(x,y)
	print(x_counter,y_counter)


def grid_partition():
	original_image = cv2.imread("wowo.png")
	gray=cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
	print(gray)
	height, width, = gray.shape
	#print(height,width)
	grid_height = height/3
	grid_width = width/3
	grid_1,grid_2,grid_3,grid_4,grid_5,grid_6,grid_7,grid_8,grid_9 = get_grid_array(gray,grid_height,grid_width)
	#print(grid_1,"\n",grid_2,"\n",grid_3,"\n",grid_4,"\n",grid_5,"\n",grid_6,"\n",grid_7,"\n",grid_8,"\n",grid_9)
	line_detection(grid_1)

grid_partition()