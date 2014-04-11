<<<<<<< HEAD
#Py3.0
oneone,onetwo,onethree,twofour,twofive,twosix,warhawk,vampire,mirage,lightning,sabre,spartan,poseidon,hercules,seafury=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
def pointadder():
	global oneone
	global onetwo
	global onethree
	global twofour
	global twofive
	global twosix
	global warhawk
	global vampire
	global mirage
	global lightning
	global sabre
	global spartan
	global poseidon
	global hercules
	global seafury
	if alpha == "1-1" or alpha.lower() == "oneone" or alpha == "11":
		oneone += score
	elif alpha == "1-2" or alpha.lower() == "onetwo" or alpha == "12":
		onetwo += score
	elif alpha == "1-3" or alpha.lower() == "onethree" or alpha == "13":
		onethree += score
	elif alpha == "2-4" or alpha.lower() == "twofour" or alpha == "24":
		twofour += score
	elif alpha == "2-5" or alpha.lower() == "twofive" or alpha == "25":
		twofive += score
	elif alpha == "2-6" or alpha.lower() == "twosix" or alpha == "26":
		twosix += score
	elif alpha.lower() == "warhawk":
		warhawk += score
	elif alpha.lower() == "vampire":
		vampire += score
	elif alpha.lower() == "mirage":
		mirage += score
	elif alpha.lower() == "lightning" or alpha.lower() == "lightening":
		lightning += score
	elif alpha.lower() == "sabre" or alpha.lower() == "saber":
		sabre += score
	elif alpha.lower() == "spartan":
		spartan += score
	elif alpha.lower() == "poseidon":
		poseidon += score
	elif alpha.lower() == "hercules":
		hercules += score
	elif alpha.lower() == "seafury" or alpha.lower() == "sea fury":
		seafury += score
	else:
		print("Sorry, I didn't understand the section")
from time import ctime	
print("Bivouac Logging Tool. V0.3.2 \n")
print("Written by Matthew Brener (akkatracker) with Javascript porting by Mitchell McMillan (mm865)")
print("Code avaliable on www.github.com/akkatracker")

with open('log.txt', 'a') as f:
	print("", file=f)
	print("----------------------NEW SESSION------------------", file=f)
	print("", file=f)
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
			score = int(input("Points Awarded: "))
			pointadder()
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
			echo = input("Echo (Current objective): ")
			score = int(input("Points Awarded (TO THE CALLING SECTION): "))
			pointadder()
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
		
		elif report.upper() == "POINTS":
			alpha = input("Section: ")
			score = int(input("Points Awarded: "))
			pointadder()
			print(ctime(),"|", score, "points added to", alpha, file = f)
		
		else:
			print("Could not detect report type, read the readme for usage")
		print("")
		report = input("Report type: ")	
	print("***Points***: 1-1:",oneone, "| 1-2:", onetwo, "| 1-3:", onethree, "| 2-4:", twofour, "| 2-5:", twofive, "| 2-6:", twosix, "| WarHawk:", warhawk, "| Vampire:", vampire, "| Mirage:", mirage, "| Lightning:", lightning, "| Sabre:", sabre, "| Spartan:", spartan, "| Poseidon:", poseidon, "| Hercules:", hercules, "| Seafury:", seafury, file = f)
=======
from time import ctime
print("Bivouac Logging Tool. V0.2 \nWritten by Matthew Brener (akkatracker)\nCode avaliable on www.github.com/akkatracker")
f=open('log.txt', 'a')
oneone,onetwo,onethree,twofour,twofive,twosix=0,0,0,0,0,0
report=input("Report type: ")
while report.lower()!="finish":
	if report.upper()=="SITREP":
		alpha,bravo,charlie,delta,echo,foxtrot,golf=input("Alpha (Callsign): "),input("Bravo (Grid): "),input("Charlie (Current objective): "),input("Delta (Level of supplies): "),input("Echo (Equipment status): "),input("Foxtrot (Morale): "),input("Golf (Comments): ")
		print(ctime(),"|",report.upper(),"| Callsign:",alpha,"| Location:",bravo,"| Current Objective:",charlie,"| Level of Supplies:",delta,"| Equipment Status:",echo,"| Morale: ",foxtrot,"| Comments: ",golf,file=f)
	elif report.upper()=="CASEVAC":
		duff,alpha,bravo,charlie,delta,echo,foxtrot,golf,hotel=input("No Duff or Exercise? "),input("Alpha (Callsign): "),input("Bravo (Grid): "),input("Charlie (Injured Person): "),input("Delta (Urgency): "),input("Echo (Nature of Injury/Illness): "),input("Foxtrot (Walking or Stretcher): "),input("Golf (Any measures required): "),input("Hotel (Comments): ")
		print(ctime(),"|",report.upper(),"| No Duff or exercise: ",duff,"| Callsign:",alpha,"| Location:",bravo,"| Injured Person:",charlie,"| Urgency:",delta,"| Injury:",echo,"| Walking or Stretcher: ",foxtrot,"| Any Measures Required: ",golf,"| Comments: ",hotel,file=f)
	elif report.upper()=="CONTACT":
		alpha,bravo,charlie,delta,echo = input("Alpha (Callsign): "),input("Bravo (Grid): "),input("Charlie (Units engaged): "),input("Delta (Successful Unit): "),input("Echo (Current objective: ")
		print(ctime(),"|",report.upper(),"| Callsign:", alpha, "| Location:",bravo,"| Units ambushed :",charlie,"| Successful Unit:",delta,"| Current objective:",echo,file=f)
	elif report.upper()=="BUSHFIRE":
		duff,alpha,bravo,charlie,delta,echo,foxtrot,golf, hotel,india,juliet,kilo,lima=input("No Duff or Exercise? "),input("Alpha (Callsign): "), input("Bravo (Grid): "), input("Charlie (Evac Required): "), input("Delta (Extent of fire): "), input("Echo (Direction and Speed of Fire Front): "),input("Foxtrot (Terrain): "),input("Golf (Number of personnel): "),input("Hotel (Level of Danger to group): "),input("India (Any action taken): "),input("Juliet (Details of casualties): "),input("Kilo (Best route to reach position): "),input("Lima (Any other info): ")
		print(ctime(),"|",report.upper(),"| No Duff or exercise: ",duff,"| Callsign:",alpha,"| Location:",bravo,"| Evac Required:",charlie,"| Fire Extent",delta,"| Speed and Direction of fire front:",echo,"| Terrain: ",foxtrot,"| Number of Personnel: ",golf,"| Level of Danger to group: ",hotel,"| Action Taken: ",india,"| Any action taken: ",juliet,"| Details of Casualties",kilo,"| Other info",lima,file=f)
	elif report.upper()=="NOTICAS":
		duff, alpha, bravo, charlie, delta, echo = input("No Duff or Exercise? "), input("Alpha (Callsign): "), input("Bravo (Grid): "), input("Charlie (Injured Person): "), input("Delta (Nature of Injury/Illness): "), input("Echo (Grid, Date, Time where injury occurred): ")
		print(ctime(),"|", report.upper(),"| No Duff or exercise: ",duff,"| Callsign:",alpha,"| Location:",bravo,"| Injured Person:",charlie,"| Injury:",delta,"| Location, Date, Time of injury:",echo,file=f)
	elif report.upper()=="FLOOD":
		duff,alpha,bravo,charlie,delta,echo,foxtrot,golf,india,juliet,kilo,lima=input("No Duff or Exercise? "),input("Alpha (Callsign): "),input("Bravo (Grid): "),input("Charlie (Evac Required): "),input("Delta (Extent of flood): "),input("Echo (Direction and Speed of Water): "),input("Foxtrot (Terrain): "),input("Golf (Number of personnel): "),input("Hotel (Further comments): "),input("India (Any action taken): "),input("Juliet (Details of casualties): "),input("Kilo (Best route to reach position): "),input("Lima (Any other info): ")
		print(ctime(),"|",report.upper(),"| No Duff or exercise: ",duff,"| Callsign:",alpha,"| Location:",bravo,"| Evac Required:",charlie,"| Flood Extent",delta,"| Speed and Direction of water:",echo, "| Terrain: ",foxtrot, "| Number of Personnel: ",golf,"| Comments: ",hotel,"| Action Taken: ",india,"| Casualties: ",juliet,"| Best Route",kilo, "| Other info",lima,file=f)
	elif report.upper()=="MAINTDEM":
		alpha,bravo,charlie,delta,echo=input("Alpha (Callsign): "),input("Bravo (Grid): "),input("Charlie (Supplies Required): "),input("Delta (Time and location resupply): "),input("Echo (Any other info): ")
		print(ctime(),"|", report.upper(),"| Callsign:", alpha,"| Location:", bravo,"| Supplies Required:",charlie,"| Location and Time of resupply",delta,"| Other:",echo,file = f)
	elif report.upper()=="LOST PERSON" or report.upper() == "LOST":
		duff,alpha,bravo,charlie,delta,echo,foxtrot,golf,hotel=input("No Duff or Exercise? "), input("Alpha (Callsign): "),input("Bravo (Grid): "),input("Charlie (Lost Person + Description): "),input("Delta (Time Location Direction of travel at last sighting): "),input("Echo (Equipment carried by lost person): "),input("Foxtrot (Assistance required): "),input("Golf (Nearest Crossroads): "),input("Hotel (Any Action Taken) :")
		print(ctime(),"|",report.upper(),"| No Duff or exercise: ",duff,"| Callsign:",alpha,"| Location:",bravo,"| Lost Person:",charlie,"| Location, Time and direction of last sighting",delta,"| Equipment:",echo,"| Assistance Required: ",foxtrot,"| Nearest crossroads: ",golf,"| Action Taken: ",hotel,file = f)
	elif report.upper()=="CHAT":
		sender,receiver,messagedetails=input("Sender: "),input("Receiver: "),input("Details of transmission: ")
		print(ctime(),"|", report.upper(),"| From:",sender,"| To:",receiver,"| Message:",messagedetails,file = f)
	report = input("Report type: ")
print("1-1:",oneone,"| 1-2:",onetwo,"| 1-3:",onethree,"| 2-4:",twofour,"| 2-5:",twofive,"| 2-6:",twosix,file=f) 
f.close()
>>>>>>> 38844a24532f7d03d48dc61daf4b7f8d083bc664
