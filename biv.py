#!/usr/bin/env python3
from time import ctime	
oneone,onetwo,onethree,twofour,twofive,twosix,alphaone,alphatwo,alphathree,bravofour,bravofive,bravosix,charlieseven,charlieeight,charlienine=0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
def pointadder():
	global oneone
	global onetwo
	global onethree
	global twofour
	global twofive
	global twosix
	global alphaone
	global alphatwo
	global alphathree
	global bravofour
	global bravofive
	global bravosix
	global charlieseven
	global charlieeight
	global charlienine
	if alpha.lower() in ("oneone", "11", "1-1"): 
		oneone += score
	elif alpha.lower() in ("1-2", "onetwo", "12"):
		onetwo += score
	elif alpha.lower() in ("1-3", "onethree", "13"):
		onethree += score
	elif alpha.lower() in ("2-4", "twofour", "24"):
		twofour += score
	elif alpha.lower() in ("2-5", "twofive", "25"):
		twofive += score
	elif alpha.lower() in ("2-6", "twosix", "26"):
		twosix += score
	elif alpha.lower() in ("a1", "a-1", "alpha 1", "alpha one"):
		alphaone += score
	elif alpha.lower() in ("a2", "a-2", "alpha 2", "alpha two"):
		alphatwo += score
	elif alpha.lower() in ("a3", "a-3", "alpha 3", "alpha three"):
		alphathree += score
	elif alpha.lower() in ("b4", "b-4", "bravo 4", "bravo four"):
		bravofour += score
	elif alpha.lower() in ("b5", "b-5", "bravofive", "bravo five"):
		bravofive += score
	elif alpha.lower() in ("b6", "b-6", "bravosix", "bravo six"):
		bravosix += score
	elif alpha.lower() in ("c7", "c-7", "charlieseven", "charlie seven"):
		charlieseven += score
	elif alpha.lower() in ("c8", "c-8", "charlieeight", "charlie eight"):
		charlieeight += score
	elif alpha.lower() in ("c9", "c-9", "charlienine", "charlie nine"):
		charlienine += score
	else:
		print("Sorry, I didn't understand the section")
print("Bivouac Logging Tool. V0.4.2 \n")
print("Written by Matthew Brener (akkatracker) with Javascript porting by Mitchell McMillan (mm865)")
print("Code avaliable on www.github.com/akkatracker")
f = open("log.txt", "a")
print("", file=f)
print("----------------------NEW SESSION------------------", file=f)
print("", file=f)
f.close()
report = input("Report type: ")
while report.lower() != "finish":
	f = open("log.txt", "a")
	if report.upper() == "SITREP":
		alpha = input("Callsign: ")
		bravo = input("Alpha (Time): ")
		charlie = input("Bravo (Own Situation): ")
		delta = input("Charlie (Situation with regard to third parties): ")
		echo = input("Delta (Future intentions and relevant info): ")
		score = int(input("Points Awarded: "))
		pointadder()
		print(ctime(),"|", report.upper(), "| Callsign:", alpha, "| Time:", bravo, "| Situation of self:", charlie, "| Situation with regard to third parties:", delta, "| Future intentions:", echo, file=f)
		
	elif report.upper() == "CASEVAC":
		duff = input("No Duff or Exercise? ")
		alpha = input("Callsign: ")
		bravo = input("Priority: ")
		charlie = input("Alpha One (Number of stretcher cases): ")
		delta = input("Alpha Two (Number of sitting cases): ")
		echo = input("Bravo (Requirement of special equipment): ")
		foxtrot = input("Charlie One (Location of Evacuation): ")
		golf = input("Charlie Two (Callsign of the ranking person with the casualty): ")
		hotel = input("Delta (Remarks): ")
		print(ctime(),"|", report.upper(), "| No Duff or exercise: ", duff, "| Callsign:", alpha, "| Priority:", bravo, "| Stretcher Cases:", charlie, "| Sitting Cases:", delta, "| Special Equipment:", echo, "| Location of evacuation: ", foxtrot, "| Callsign of ranking person with injury: ", golf, "| Remarks: ", hotel, file=f)
		
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
		alpha = input("Callsign: ")
		bravo = input("Alpha (Rank of Casualty): ")
		charlie = input("Bravo (Name): ")
		delta = input("Charlie (Nature of Injury/Illness): ")
		echo = input("Delta (Grid where injury occurred): ")
		foxtrot = input("Echo (Time of injury): ")
		golf = input("Foxtrot (Any treatment administered): ")
		hotel = input("Golf (Remarks and present location): ")
		print(ctime(),"|", report.upper(), "| No Duff or exercise: ", duff, "| Callsign:", alpha, "| Rank of Casualty:", bravo, "| Injured Person:", charlie, "| Injury:", delta, "| Location of injury:", echo, "| Time of injury:", foxtrot, "| Treatment administered:", golf, "| Location and remarks:", hotel, file=f)
		
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
		alpha = input("Callsign: ")
		bravo = input("Alpha (Demand Number): ")
		charlie = input("Bravo (Priority): ")
		delta = input("Charlie One (Quantity of meal packs): ")
		echo = input("Charlie Two (Quantity of jerries): ")
		foxtrot = input("Charlie Three (Quantity of fruit): ")
		golf = input("Charlie Four (Other items and quantities): ")
		hotel = input("Location of delivery (Grid): ")
		india = input("Time of delivery: ")
		juliet = input("Mode of delivery: ")
		kilo = input("Remarks: ")
		print(ctime(),"|", report.upper(), "| Callsign:", alpha, "| Demand number:", bravo, "| Priority:", charlie, "| Meal Packs", delta, "| Jerries:", echo, "| Fruit:", foxtrot, "| Other:", golf, "| Location:", hotel, "| Time:", india, "| Mode:", juliet, "| Remarks:", kilo, file = f)
		
	elif report.upper() in ("LOST PERSON", "LOST"):
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
	
	elif report.upper() in ("STRENGTH STATE", "STRENGTH", "STRSTAT"):
		alpha = input("Section: ")
		bravo = input("Alpha One (Number of own cadets): ")
		charlie = input("Alpha Two (Number of attachments): ")
		delta = input("Alpha Three (Number of airmen or officers): ")
		echo = input("Bravo One (Number of expected attachments in 24 hours): ")
		foxtrot = input("Bravo Two (Number of expected detachments in 24 hours): ")
		golf = input("Charlie (Total number of personnel): ")
		print(ctime(),"| Callsign:", alpha, "| Number of own cadets:", bravo, "| Number of attachments:", charlie, "| Number of airmen or officers:", delta, "| Number of expected attachments in 24 hours:", echo, "| Number of expected detachments in 24 hours:", foxtrot, "| Total number of personnel:", golf, file = f)
		
	elif report.upper() in ("LOCSTAT", "LOCATION"):
		alpha = input("Section: ")
		bravo = input("Alpha (Grid): ")
		charlie = input("Bravo (Stationary or moving): ")
		delta = input("Charlie (Direction of movement or predicted length of halt): ")
		print(ctime(),"| Callsign:", alpha, "| Location:", bravo, "| Stationary or moving:", charlie, "| Direction of movement or predicted length of halt:", delta, file = f)
	
	elif report.upper() in ("INTREP", "INCIDENT", "INCIDENT REPORT"):
		alpha = input("Section: ")
		bravo = input("Alpha (Time of incident): ")
		charlie = input("Bravo (Location of incident): ")
		delta = input("Charlie (Description of incident): ")
		echo = input("Delta (Commander's evaluation of incident): ")
		print(ctime(),"| Callsign:", alpha, "| Time of incident:", bravo, "| Location of incident:", charlie, "| Description of incident:", delta, "| Commander's evaluation", echo, file = f)
	else:
		print("Could not detect report type, read the readme for usage")
	print("")
	report = input("Report type: ")	
	print("***Points***: 1-1:",oneone, "| 1-2:", onetwo, "| 1-3:", onethree, "| 2-4:", twofour, "| 2-5:", twofive, "| 2-6:", twosix, "| Alpha 1:", alphaone, "| Alpha 2:", alphatwo, "| Alpha 3:", alphathree, "| Bravo 1:", bravofour, "| Bravo 2:", bravofive, "| Bravo 3:", bravosix, "| Charlie 1:", charlieseven, "| Charlie 2:", charlieeight, "| Charlie 3:", charlienine, file = f)
	f.close()