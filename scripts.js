function sitrep(){
	var output = document.getElementById('output').value,
		time = new Date(),
		time = String(time),
		time = time.substring(0, 21),
		alpha = document.getElementById('sitrep_callsign').value,
		bravo = document.getElementById('sitrep_grid').value,
		charlie = document.getElementById('sitrep_objective').value,
		delta = document.getElementById('sitrep_supplies').value,
		echo = document.getElementById('sitrep_equipment').value,
		foxtrot = document.getElementById('sitrep_morale').value,
		golf = document.getElementById('sitrep_comments').value,
		out = time + " | SITREP | Callsign: " + alpha + " | Location:" + bravo + " | Current Objective: " + charlie + " | Level of Supplies: " + delta + " | Equipment Status: " + echo + " | Morale: " + foxtrot + " | Comments: "+ golf +'\n';
	document.getElementById('output').value = output  + out;
	document.getElementById('sitrep_callsign').value ='';
	document.getElementById('sitrep_grid').value ='';
	document.getElementById('sitrep_objective').value='';
	document.getElementById('sitrep_supplies').value='';
	document.getElementById('sitrep_equipment').value='';
	document.getElementById('sitrep_morale').value='';
	document.getElementById('sitrep_comments').value='';
};