def data(positions):
	rules_list=[[1, 1, 3, 1, 0, 2, 1, 3, 1], [2, 1, 3, 1, 0, 1, 1, 3, 1], [1, 2, 1, 1, 0, 1, 1, 3, 1], [1, 2, 2, 1, 0, 1, 1, 3, 1], [1, 1, 3, 1, 0, 1, 1, 3, 1], [2, 2, 1, 1, 0, 1, 1, 3, 1], [0, 2, 0, 1, 0, 1, 1, 3, 1], [3, 1, 3, 1, 0, 1, 1, 3, 1], [2, 0, 2, 1, 0, 1, 1, 3, 1], 
				[2, 0, 0, 2, 0, 0, 0, 0, 0], [2, 0, 0, 2, 0, 0, 1, 3, 3], [1, 3, 1, 2, 0, 1, 1, 3, 1], [0, 2, 0, 3, 1, 3, 0, 0, 0], 
				[1, 0, 0, 2, 0, 3, 1, 0, 0], [1, 0, 1, 2, 1, 3, 1, 0, 0], [1, 2, 0, 2, 0, 3, 1, 0, 0], [1, 0, 0, 2, 0, 0, 1, 0, 0], [1, 0, 2, 2, 0, 3, 1, 0, 0],
				[1, 3, 3, 1, 3, 3, 0, 0, 0], [2, 0, 1, 1, 0, 1, 1, 3, 1], 
				[1, 3, 1, 1, 0, 1, 1, 1, 2], [2, 0, 1, 1, 2, 1, 1, 0, 2], [2, 1, 1, 1, 1, 1, 1, 1, 2], [2, 0, 1, 1, 1, 1, 1, 1, 2], [2, 2, 1, 1, 2, 1, 1, 2, 2], [2, 1, 1, 1, 2, 1, 1, 1, 2], [2, 0, 1, 1, 1, 1, 1, 2, 2], [2, 1, 1, 1, 2, 1, 1, 0, 2], [0, 0, 1, 1, 1, 1, 1, 2, 2], [0, 0, 1, 1, 2, 1, 1, 1, 0],
				[0, 2, 0, 3, 1, 3, 3, 1, 3], 
				[1, 3, 1, 1, 2, 1, 1, 1, 3], [1, 3, 1, 1, 1, 1, 1, 0, 1], [1, 3, 1, 1, 1, 1, 1, 0, 0], [1, 3, 1, 1, 1, 1, 0, 0, 2], [1, 3, 1, 1, 2, 1, 1, 0, 2], [1, 3, 1, 1, 1, 1, 1, 2, 3], [1, 3, 1, 1, 0, 1, 3, 1, 1], [1, 3, 1, 1, 2, 1, 1, 0, 1], 
				[1, 3, 1, 1, 1, 1, 1, 2, 1], [1, 3, 1, 1, 1, 1, 1, 1, 1], [1, 3, 1, 1, 2, 1, 1, 2, 1], [1, 3, 1, 1, 2, 1, 1, 1, 1], 
				[1, 2, 1, 1, 2, 2, 0, 0, 0], [1, 0, 1, 1, 2, 0, 2, 2, 2], [0, 2, 1, 1, 2, 1, 2, 2, 2], [2, 0, 1, 1, 2, 1, 0, 0, 2], [0, 0, 1, 1, 2, 1, 0, 0, 2], [0, 0, 1, 1, 2, 1, 1, 0, 2], [0, 2, 1, 1, 2, 1, 0, 0, 2], [2, 2, 2, 1, 2, 0, 1, 2, 2], [1, 1, 1, 1, 2, 0, 0, 2, 0], [0, 0, 1, 1, 2, 2, 0, 2, 1], [1, 0, 1, 1, 2, 1, 0, 0, 2], [2, 0, 1, 1, 2, 2, 0, 0, 2], [0, 0, 1, 1, 2, 2, 1, 0, 2], [1, 0, 1, 1, 2, 0, 2, 1, 2], [2, 2, 1, 2, 2, 1, 0, 0, 2], [0, 0, 1, 1, 2, 2, 0, 2, 2], [2, 2, 1, 1, 2, 2, 0, 0, 2], 
				[2, 2, 1, 0, 2, 0, 3, 1, 3], [2, 0, 1, 2, 2, 0, 3, 1, 3], [2, 0, 2, 1, 1, 3, 3, 1, 3], [2, 0, 1, 0, 2, 0, 3, 1, 3], [0, 0, 0, 3, 1, 3, 3, 1, 3], [2, 2, 1, 0, 2, 2, 3, 1, 3], [2, 1, 0, 2, 1, 3, 3, 1, 3], [2, 0, 0, 0, 1, 3, 3, 1, 3], [1, 1, 1, 0, 2, 0, 3, 1, 3], [2, 0, 1, 0, 2, 2, 3, 1, 3], [2, 2, 0, 0, 1, 3, 3, 1, 3], 
				[0, 0, 2, 1, 0, 3, 0, 0, 0], [0, 0, 1, 0, 2, 2, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 2, 0, 0, 0], [0, 0, 2, 0, 1, 3, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 2, 3, 0, 0, 0], [0, 0, 1, 2, 2, 2, 0, 0, 0], [0, 0, 1, 3, 1, 1, 2, 0, 0], [0, 0, 1, 2, 2, 0, 1, 0, 0], 
				[2, 0, 1, 2, 0, 1, 0, 0, 1], [2, 0, 1, 2, 0, 1, 0, 0, 0], [2, 0, 0, 2, 0, 1, 0, 0, 0], 
				[2, 0, 0, 1, 3, 3, 0, 0, 0], [2, 0, 0, 1, 3, 3, 2, 0, 0], [0, 0, 0, 1, 3, 3, 0, 0, 0], [1, 0, 0, 1, 3, 3, 0, 0, 0], [1, 0, 0, 1, 3, 3, 2, 0, 0],
				[2, 0, 1, 1, 3, 1, 0, 0, 1], [2, 0, 0, 1, 3, 1, 0, 0, 2], [2, 0, 1, 1, 3, 1, 0, 0, 2] ,[2, 0, 1, 1, 3, 1, 0, 0, 0], [2, 0, 0, 1, 3, 1, 0, 0, 0], [2, 0, 0, 1, 0, 1, 0, 0, 2], 
				[0, 0, 0, 1, 0, 0, 0, 0, 1], [2, 0, 0, 1, 0, 0, 0, 0, 2], [2, 0, 2, 1, 3, 0, 0, 0, 2], [2, 0, 3, 1, 0, 0, 2, 0, 2], [2, 0, 2, 1, 0, 0, 0, 0, 2], [2, 0, 0, 1, 0, 0, 0, 0, 0], [2, 0, 0, 1, 0, 0, 0, 0, 1], 
				[0, 2, 0, 0, 1, 3, 1, 1, 3], [0, 2, 0, 0, 1, 3, 1, 2, 3], [0, 2, 0, 0, 1, 3, 0, 1, 3], [0, 2, 0, 1, 1, 3, 0, 1, 3], 
				[2, 0, 0, 1, 3, 1, 1, 0, 2], [0, 0, 1, 1, 3, 1, 1, 0, 2], [1, 0, 1, 1, 3, 1, 1, 0, 2], [2, 0, 0, 1, 3, 1, 2, 0, 1], [1, 0, 1, 1, 3, 1, 0, 0, 1], 
				[2, 0, 1, 2, 0, 0, 1, 3, 3], [2, 0, 1, 1, 0, 0, 1, 3, 3], 
				[0, 0, 1, 2, 0, 1, 0, 0, 2], [2, 0, 1, 1, 0, 1, 0, 0, 2], [2, 0, 2, 1, 1, 1, 0, 0, 2], 
				[2, 1, 3, 2, 2, 0, 1, 0, 2], [2, 2, 1, 2, 2, 1, 1, 2, 0], [2, 2, 1, 2, 2, 1, 1, 0, 0], [2, 1, 3, 2, 2, 2, 1, 0, 2], [2, 0, 1, 2, 2, 1, 1, 0, 0], [2, 1, 3, 2, 1, 3, 1, 0, 0], [2, 2, 1, 2, 2, 0, 1, 0, 0], [2, 1, 3, 2, 0, 3, 1, 0, 0], 
				[2, 0, 0, 0, 0, 0, 0, 0, 2], [1, 0, 0, 0, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 2, 0, 0, 0], [0, 0, 0, 0, 0, 2, 0, 0, 2], [0, 0, 0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0, 0], 
				[1, 3, 1, 1, 3, 1, 2, 0, 1], [1, 3, 1, 1, 3, 1, 1, 0, 2], [1, 3, 1, 1, 3, 1, 0, 0, 2], [1, 3, 1, 1, 3, 1, 1, 0, 1]]
	charlist = ["A","A","A","A","A","A","A","A","A",
				"E","F","H","I","K","K","K","K","K","L","M","N","N","N","N","N","N","N","N","N","N","T",
				"V","V","V","V","V","V","V","V",
				"W","W","W","W","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X",
				"Y","Y","Y","Y","Y","Y","Y","Y","Y","Y","Y",
				"Z","Z","Z","Z","Z","Z","Z","Z","Z","Z",
				"B","B","B","C","C","C","C","C",
				"D","D","D","D","D","D", 
				"G","G","G","G","G","G","G",
				"J","J","J","J", 
				"O","O","O","O","O", 
				"P","P", 
				"Q","Q","Q", 
				"R","R","R","R","R","R","R","R", 
				"S","S","S","S","S","S", 
				"U","U","U","U"]
	for index,rule in enumerate(rules_list):
		if rule==positions:
			print(charlist[index])
			return charlist[index]
