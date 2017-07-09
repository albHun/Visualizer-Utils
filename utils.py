def absToRel(interList, type = "mm"):
	if type == "mm":
		mmRelaList = list()
		starting_time = 0.0
		for mmIndex in range(len(interList)):
			curCoor = interList[mmIndex][0]
			curTime = interList[mmIndex][1]
			starting_time = curTime
			if mmIndex == 0:
				mmRelaList.append(([curCoor, 0]))
			else:
				prevCoor = interList[mmIndex-1][0]
				prevTime = interList[mmIndex-1][1]
				mmRelaList.append(((curCoor[0] - prevCoor[0], curCoor[1] - prevCoor[1]), curTime - prevTime))
		return mmRelaList, starting_time

	if type == "mc": # mouse click
		mcRelaList = list()
		starting_time = 0.0
		click_time = 0
		mouse_down = 0
		mouse_up = 0
		if interList[0]["type"] == "mu":
			print("Not handled mouse click between chunks at ", interList[0]["coor"], " at ", interList[0]["time"])
			del interList[0]
			
		starting_time = interList[0]["time"]
		
		for mouse_inter_index in range(len(interList)):
			if interList[mouse_inter_index]["type"] == "md":
				mouse_down = interList[mouse_inter_index]
				click_time = mouse_down["time"]
			else:
				mouse_up = interList[mouse_inter_index]
				click_duration = mouse_up["time"] - mouse_down["time"]
				mcRelaList.append((click_time, mouse_down["coor"], click_duration))		