import recognize_character as recog
import bfs_segment as segmentation
def check_rules():
	charlist = ["A.png","E.png","F.png","H.png","I.png","K.png","L.png","M.png","N.png","T.png","V.png","W.png","X.png","Y.png","Z.png"]
	rules = []
	for alphabet in charlist:
		segmentation.main("alphabets/"+str(alphabet))
		character_rule=recog.main()
		rules.append(character_rule)
	print(rules)
def detect_character(training_data,filename):
	segmentation.main(filename)
	train_data=training_data.read()
	character_rule, character_name =recog.main()
	print(character_name,character_rule)
	if character_name==None and str(character_rule) not in str(train_data):
		training_data.write(str(character_rule)+"\n")

def train():
	training_data=open("train.txt","a+")
	for i in range(1,11):
		filename="train/"+str(i)+".png"
		detect_character(training_data,filename)

def Recognize():
	output = open("output.txt","a+")
	first_coordinate_past,character_width_past = segmentation.main("ggl.png")
	character_rule, character_name =recog.main()
	print(character_name,character_rule)
	output.write(character_name)
	output.close()
	return first_coordinate_past,character_width_past

def Compleate_Recognition(first_coordinate_past,character_width_past):
	output = open("output.txt","a+")
	first_coordinate_present,character_width_present = segmentation.main("temp.png")
	character_rule, character_name =recog.main()
	print(character_name,character_rule)
	if first_coordinate_present[1]>first_coordinate_past[1]:
		output.write("\n")
	# if first_coordinate_present[0]>(first_coordinate_past[0]+(50*character_width_past)):
	# 	output.write(" ")
	first_coordinate_past=first_coordinate_present
	character_width_past=character_width_present
	output.write(character_name)
	output.close()
	return first_coordinate_past,character_width_past
first_coordinate_past,character_width_past= Recognize()
while True:
	try:
		first_coordinate_past,character_width_past = Compleate_Recognition(first_coordinate_past,character_width_past)
	except IndexError:
		break
#train()