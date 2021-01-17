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
def detect_character():
	segmentation.main("iii.png")
	character_rule, character_name =recog.main()
	print(character_name,character_rule)
detect_character()