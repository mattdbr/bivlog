from time import ctime
print("Bivouac Logging Tool. V0.2 \nWritten by Matthew Brener (akkatracker)\nCode avaliable on www.github.com/akkatracker")
f = open('log.txt', 'a')
# exercise = input("What exercise is this? ")
# if exercise.upper() == "NAVEX":
	# print("You chose Navex")
report = input("Report type: ")
while report.lower() != "finish":

	if report.upper() == "SITREP":
		alpha = input("Alpha (Callsign): ")
		bravo = input("Bravo (Grid): ")
		charlie = input("Charlie (Current objective): ")
		delta = input("Delta (Level of supplies): ")
		echo = input("Echo (Equipment status): ")
		foxtrot = input("Foxtrot (Morale): ")
		golf = input("Golf (Comments): ")
		print(ctime(),"|", report.upper(), "| Callsign:", alpha, "| Location:", bravo, "| Current Objective:", charlie, "| Level of Supplies:", delta, "| Equipment Status:", echo, "| Morale: ", foxtrot, "| Comments: ", golf, file=f)
		
	elif report.upper() == "CASEVAC":
		duff = input("No Duff or Exercise? ")
		alpha = input("Alpha (Callsign): ")
		bravo = input("Bravo (Grid): ")
		charlie = input("Charlie (Injured Person): ")
		delta = input("Delta (Urgency): ")
		echo = input("Echo (Nature of Injury/Illness): ")
		foxtrot = input("Foxtrot (Walking or Stretcher): ")
		golf = input("Golf (Any measures required): ")
		hotel = input("Hotel (Comments): ")
		print(ctime(),"|", report.upper(), "| No Duff or exercise: ", duff, "| Callsign:", alpha, "| Location:", bravo, "| Injured Person:", charlie, "| Urgency:", delta, "| Injury:", echo, "| Walking or Stretcher: ", foxtrot, "| Any Measures Required: ", golf, "| Comments: ", hotel, file=f)
		
	elif report.upper() == "CONTACT":
		alpha = input("Alpha (Callsign): ")
		bravo = input("Bravo (Grid): ")
		charlie = input("Charlie (Units engaged): ")
		delta = input("Delta (Successful Unit): ")
		echo = input("Echo (Current objective: ")
		print(ctime(),"|", report.upper(), "| Callsign:", alpha, "| Location:", bravo, "| Units ambushed :", charlie, "| Successful Unit:", delta, "| Current objective:", echo, file=f)
		
	elif report.upper() == "BUSHFIRE":
		duff = input("No Duff or Exercise? ")
		alpha = input("Alpha (Callsign): ")
		bravo = input("Bravo (Grid): ")
		charlie = input("Charlie (Evac Required): ")
		delta = input("Delta (Extent of fire): ")
		echo = input("Echo (Direction and Speed of Fire Front): ")
		foxtrot = input("Foxtrot (Terrain): ")
		golf = input("Golf (Number of personnel): ")
		hotel = input("Hotel (Level of Danger to group): ")
		india = input("India (Any action taken): ")
		juliet = input("Juliet (Details of casualties): ")
		kilo = input("Kilo (Best route to reach position): ")
		lima = input("Lima (Any other info): ")
		print(ctime(),"|",report.upper(), "| No Duff or exercise: ", duff,"| Callsign:",alpha, "| Location:",bravo,"| Evac Required:",charlie,"| Fire Extent", delta, "| Speed and Direction of fire front:",echo, "| Terrain: ",foxtrot, "| Number of Personnel: ",golf,"| Level of Danger to group: ",hotel, "| Action Taken: ", india,"| Any action taken: ",juliet,"| Details of Casualties",kilo, "| Other info",lima, file=f)
		
	elif report.upper() == "NOTICAS":
		duff = input("No Duff or Exercise? ")
		alpha = input("Alpha (Callsign): ")
		bravo = input("Bravo (Grid): ")
		charlie = input("Charlie (Injured Person): ")
		delta = input("Delta (Nature of Injury/Illness): ")
		echo = input("Echo (Grid, Date, Time where injury occurred): ")
		print(ctime(),"|", report.upper(), "| No Duff or exercise: ", duff, "| Callsign:", alpha, "| Location:", bravo, "| Injured Person:", charlie, "| Injury:", delta, "| Location, Date, Time of injury:", echo, file=f)
		
	elif report.upper() == "FLOOD":
		duff = input("No Duff or Exercise? ")
		alpha = input("Alpha (Callsign): ")
		bravo = input("Bravo (Grid): ")
		charlie = input("Charlie (Evac Required): ")
		delta = input("Delta (Extent of flood): ")
		echo = input("Echo (Direction and Speed of Water): ")
		foxtrot = input("Foxtrot (Terrain): ")
		golf = input("Golf (Number of personnel): ")
		hotel = input("Hotel (Further comments): ")
		india = input("India (Any action taken): ")
		juliet = input("Juliet (Details of casualties): ")
		kilo = input("Kilo (Best route to reach position): ")
		lima = input("Lima (Any other info): ")
		print(ctime(),"|", report.upper(), "| No Duff or exercise: ", duff, "| Callsign:", alpha, "| Location:", bravo, "| Evac Required:", charlie, "| Flood Extent", delta, "| Speed and Direction of water:", echo, "| Terrain: ", foxtrot, "| Number of Personnel: ", golf, "| Comments: ", hotel, "| Action Taken: ", india, "| Casualties: ", juliet, "| Best Route", kilo, "| Other info",lima, file=f)
		
	elif report.upper() == "MAINTDEM":
		alpha = input("Alpha (Callsign): ")
		bravo = input("Bravo (Grid): ")
		charlie = input("Charlie (Supplies Required): ")
		delta = input("Delta (Time and location resupply): ")
		echo = input("Echo (Any other info): ")
		print(ctime(),"|", report.upper(), "| Callsign:", alpha, "| Location:", bravo, "| Supplies Required:", charlie, "| Location and Time of resupply", delta, "| Other:", echo, file = f)
		
	elif report.upper() == "LOST PERSON" or report.upper() == "LOST":
		duff = input("No Duff or Exercise? ")
		alpha = input("Alpha (Callsign): ")
		bravo = input("Bravo (Grid): ")
		charlie = input("Charlie (Lost Person + Description): ")
		delta = input("Delta (Time Location Direction of travel at last sighting): ")
		echo = input("Echo (Equipment carried by lost person): ")
		foxtrot = input("Foxtrot (Assistance required): ")
		golf = input("Golf (Nearest Crossroads): ")
		hotel = input("Hotel (Any Action Taken) :")
		print(ctime(),"|", report.upper(), "| No Duff or exercise: ", duff, "| Callsign:", alpha, "| Location:", bravo, "| Lost Person:", charlie, "| Location, Time and direction of last sighting", delta, "| Equipment:", echo, "| Assistance Required: ", foxtrot, "| Nearest crossroads: ", golf, "| Action Taken: ", hotel, file = f)
	
	elif report.upper() == "CHAT":
		sender = input("Sender: ")
		receiver = input("Receiver: ")
		messagedetails = input("Details of transmission: ")
		print(ctime(),"|", report.upper(), "| From:", sender, "| To:", receiver, "| Message:", messagedetails, file = f)
	report = input("Report type: ")
f.close()			