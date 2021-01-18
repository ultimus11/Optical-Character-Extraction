import cv2
import numpy as np
import matplotlib.pyplot as plt
class check_continuity():
	def __init__(self, filename):
		self.filename = filename
		self.img=np.array(cv2.imread(filename))
		self.character_list=[]
	#check position of colour position in image
	def find_position(self,colour,image):
		character_list = self.character_list
		xposition=0
		yposition=0
		for y in image:
			xposition=0
			for x in y:
				if x==0:
					#print(xposition,yposition)
					character_list.append([xposition,yposition])
				xposition+=1
			yposition+=1
	def bfs(self):
		character_list=self.character_list
		print(character_list)
		contineous_region=[]
		found_contineous_elements=[]
		contineous_region_idx=0
		contineous_region.append(character_list[0])
		print(contineous_region)
		found_contineous_elements.append(contineous_region[0])
		while found_contineous_elements:
			found_contineous_elements=[]
			try:
				current_coordinate = contineous_region[contineous_region_idx]
			except IndexError:
				break
			for element in character_list:
				if (element[0]==current_coordinate[0]+1 or element[0]==current_coordinate[0]-1 or element[0]==current_coordinate[0]) and (element[1]==current_coordinate[1]+1 or element[1]==current_coordinate[1]-1 or element[1]==current_coordinate[1]):
					found_contineous_elements.append(element)
			print(found_contineous_elements)
			if found_contineous_elements:
				for found_element in found_contineous_elements:
					if found_element not in contineous_region:
						contineous_region.append(found_element)
			contineous_region_idx+=1
		#print(contineous_region)
		return contineous_region
def create_image(contineous_region):
	xlist=[]
	ylist=[]
	#stretch_near = cv2.resize(np.float32(stack1),(10, 10),interpolation=cv2.INTER_NEAREST)
	#print(stretch_near)
	for data in contineous_region:
		print(data)
		xlist.append(data[0])
		ylist.append(data[1])
	#plt.plot(xpoints, ypoints)

	minx=min(xlist)
	maxx=max(xlist)
	miny=min(ylist)
	maxy=max(ylist)
	Width=(maxx)-(minx)
	hight=(maxy)-(miny)
	pixel_coordinates=[]
	new_stack=[]
	for data in contineous_region:
		pixel_coordinates=[]
		pixel_coordinates.insert(0,data[1]-(miny))
		pixel_coordinates.insert(0,data[0]-(minx))
		new_stack.append(pixel_coordinates)
	#print("printing stack1",stack1,"\nprinting stack2",new_stack)
	# Create a blank 20x20 black image
	image = np.zeros((hight+1, Width+1, 1), np.uint8)
	# Fill image with white color(set each pixel to white)
	image[:] = (255)

	#fill pixels in image
	for data in new_stack:
		image[data[1],data[0]]=(0)
	fixed_size_image = cv2.resize(image, (30, 30),interpolation = cv2.INTER_NEAREST)
	cv2.imwrite("character.png",fixed_size_image)
	plt.plot(xlist, ylist,"ro")
	plt.axis([0, 20, 0, 20])
	plt.show()
def main(filename):
	continuity=check_continuity(str(filename))
	img=continuity.img
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	print(gray)
	continuity.find_position([0],gray)
	print(continuity.character_list)
	length = len(continuity.character_list)
	print(length)
	contineous_region = continuity.bfs()
	print(contineous_region)
	create_image(contineous_region)

if __name__=="__main__":
	main("H.png")