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
