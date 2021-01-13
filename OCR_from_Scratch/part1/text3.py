import cv2
import numpy as np
import matplotlib.pyplot as plt
img=np.array(cv2.imread("s.png"))
character_list=[]
#check position of colour position in image
def find_position(colour,image):
	global character_list
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
#check colour at given position in image
def check_colour(xposition,yposition,image):
	xposition_1=0
	yposition_1=0
	for y in image:
		xposition_1=0
		for x in y:
			if xposition==xposition_1 and yposition==yposition_1:
				return x
			xposition_1+=1
		yposition_1+=1
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print(gray)
find_position([0],gray)
print(character_list)
length = len(character_list)
def search_neighbours(CurrentX,CurrentY):
	global gray
	stack=[]
	p0 =[CurrentX,CurrentY]
	p1 =[CurrentX-1,CurrentY-1]
	p2 =[CurrentX, CurrentY-1]
	p3 =[CurrentX+1,CurrentX-1]
	p4 =[CurrentX-1,CurrentY]
	p5 =[CurrentX+1,CurrentY]
	p6 =[CurrentX-1,CurrentY+1]
	p7 =[CurrentX,CurrentY+1]
	p8 =[CurrentX+1,CurrentY+1]
	colour = check_colour(p0[0],p0[1],gray)
	if colour == 0:
		stack.insert(0,p0)
	colour = check_colour(p1[0],p1[1],gray)
	if colour == 0:
		stack.insert(0,p1)
	colour = check_colour(p2[0],p2[1],gray)
	if colour == 0:
		stack.insert(0,p2)
	colour = check_colour(p3[0],p3[1],gray)
	if colour == 0:
		stack.insert(0,p3)
	colour = check_colour(p4[0],p4[1],gray)
	if colour == 0:
		stack.insert(0,p4)
	colour = check_colour(p5[0],p5[1],gray)
	if colour == 0:
		stack.insert(0,p5)
	colour = check_colour(p6[0],p6[1],gray)
	if colour == 0:
		stack.insert(0,p6)
	colour = check_colour(p7[0],p7[1],gray)
	if colour == 0:
		stack.insert(0,p7)
	colour = check_colour(p8[0],p8[1],gray)
	if colour == 0:
		stack.insert(0,p8)
	print(stack)
	return stack
def continuity(continuity_check,neighbours):
	xy=0
	for lists in neighbours:
		print(lists)
		if lists[0]==continuity_check[0] or lists[0]==continuity_check[0]+1 or lists[0]==continuity_check[0]-1:
			print(lists[0])
			xy=1
		if lists[1]==continuity_check[1] or lists[1]==continuity_check[1]+1 or lists[1]==continuity_check[1]-1:
			print(lists[1])
		else:
			xy=0
		if xy==1:
			return True

stack1=[]
character_list_duplicate=[]
def check_neighbours_main(starting_xy,character_list):
	global stack1
	global character_list_duplicate
	#testlist=character_list.copy()
	testlist=character_list
	stack=[]
	stack.insert(0,starting_xy)
	neighbours=search_neighbours(starting_xy[0],starting_xy[1])
	try:
		for element in neighbours:
			if element in testlist:
				testlist.remove(element)
	except:
		return stack1
	print(testlist)
	continuity_check=testlist[0]
	print("printing x continuity",continuity_check[0],continuity_check[1])
	#append neighbours into stack1
	for coordinates in neighbours:
		if coordinates not in stack1:
			stack1.append(coordinates)
	continuity_result = continuity(continuity_check,stack1)
	print(continuity_result)
	if continuity_result==True:
		#stack1.append(neighbours)
		check_neighbours_main(testlist[0],testlist)
print("outside")
character_list_duplicate=character_list.copy()
try:
	whatever_returned = check_neighbours_main(character_list[0],character_list_duplicate)
except:
	print("wohoooo")
print("done",stack1)
xlist=[]
ylist=[]
for data in stack1:
	print(data)
	xlist.append(data[0])
	ylist.append(data[1])
#plt.plot(xpoints, ypoints)
plt.plot(xlist, ylist,"ro")
plt.axis([0, 20, 0, 20])
plt.show()