function printoutput(){
    document.getElementById('bigthing').style.display = 'none';
    document.getElementById('printtext').style.display = 'block';
    var content = document.getElementById('output').value,
        content = content.replace(/\n/gi, '<br>');
    document.getElementById('printtext').innerHTML = content;
    window.print();
    document.getElementById('printtext').style.display = 'none';
    document.getElementById('bigthing').style.display = 'block';
}
function sitrep(){
    var alpha = document.getElementById('sitrep_callsign').value,
        bravo = document.getElementById('sitrep_grid').value,
        charlie = document.getElementById('sitrep_objective').value,
        delta = document.getElementById('sitrep_supplies').value,
        echo = document.getElementById('sitrep_equipment').value,
        foxtrot = document.getElementById('sitrep_morale').value,
        golf = document.getElementById('sitrep_comments').value,
        output = document.getElementById('output').value,
        time = new Date(),
        time = String(time),
        time = time.substring(0, 21),
        out = time + " | SITREP | Callsign: " + alpha + " | Location:" + bravo + " | Current Objective: " + charlie + " | Level of Supplies: " + delta + " | Equipment Status: " + echo + " | Morale: " + foxtrot + " | Comments: "+ golf +'\n';
    document.getElementById('output').value = output  + out;
    document.getElementById('sitrep_callsign').value = '';
    document.getElementById('sitrep_grid').value = '';
    document.getElementById('sitrep_objective').value = '';
    document.getElementById('sitrep_supplies').value = '';
    document.getElementById('sitrep_equipment').value = '';
    document.getElementById('sitrep_morale').value = '';
    document.getElementById('sitrep_comments').value = '';
};
function casevac(){
    var duff = document.getElementById('casevac_duff').value,
        alpha = document.getElementById('casevac_callsign').value,
        bravo = document.getElementById('casevac_grid').value,
        charlie = document.getElementById('casevac_person').value,
        delta = document.getElementById('casevac_urgency').value,
        echo = document.getElementById('casevac_nature').value,
        foxtrot = document.getElementById('casevac_movement').value,
        golf = document.getElementById('casevac_measure').value,
        hotel = document.getElementById('casevac_comments').value,
        output = document.getElementById('output').value,
        time = new Date(),
        time = String(time),
        time = time.substring(0, 21),
        out = time + ' | CASEVAC | No Duff or exercise: ' + duff + " | Callsign: " + alpha + " | Location: " +  bravo + " | Injured Person: " + charlie + " | Urgency: " + delta + " | Injury: " + echo + " | Walking or Stretcher: " + foxtrot + " | Any Measures Required: " + golf + " | Comments: " + hotel + '\n';
    document.getElementById('output').value = output  + out;
    document.getElementById('casevac_duff').value = '';
    document.getElementById('casevac_callsign').value = '';
    document.getElementById('casevac_grid').value = '';
    document.getElementById('casevac_person').value = '';
    document.getElementById('casevac_urgency').value = '';
    document.getElementById('casevac_nature').value = '';
    document.getElementById('casevac_movement').value = '';
    document.getElementById('casevac_measure').value = '';
    document.getElementById('casevac_comments').value = '';
};
function contact(){
    var alpha = document.getElementById('contact_callsign').value,
        bravo = document.getElementById('contact_grid').value,
        charlie = document.getElementById('contact_units').value,
        delta = document.getElementById('contact_success').value,
        echo = document.getElementById('contact_objective').value,
        output = document.getElementById('output').value,
        time = new Date(),
        time = String(time),
        time = time.substring(0, 21),
        out = time + ' | Contact | Callsign: ' + alpha + " | Location: " +  bravo + " | Units involved: " + charlie + " | Successful unit : " + delta + " | Current objective: " + echo + '\n';
    document.getElementById('output').value = output  + out;
    document.getElementById('contact_callsign').value = '';
    document.getElementById('contact_grid').value = '';
    document.getElementById('contact_units').value = '';
    document.getElementById('contact_success').value = '';
    document.getElementById('contact_objective').value = '';
};
function bushfire(){
    var duff = document.getElementById('bushfire_duff').value,
        alpha = document.getElementById('bushfire_callsign').value,
        bravo = document.getElementById('bushfire_grid').value,
        charlie = document.getElementById('bushfire_evac').value,
        delta = document.getElementById('bushfire_extent').value,
        echo = document.getElementById('bushfire_direcspeed').value,
        foxtrot = document.getElementById('bushfire_terrain').value,
        golf = document.getElementById('bushfire_numberperson').value,
        hotel = document.getElementById('bushfire_danger').value,
        india = document.getElementById('bushfire_actiontaken').value,
        juliet = document.getElementById('bushfire_casualties').value,
        kilo = document.getElementById('bushfire_route').value,
        lima = document.getElementById('bushfire_info').value,
        output = document.getElementById('output').value,
        time = new Date(),
        time = String(time),
        time = time.substring(0, 21),
        out = time + ' | Bushfire | No Duff or exercise: ' + duff + " | Callsign: " + alpha + " | Location: " +  bravo + " | Evacuation required: " + charlie + " | Extent of fire: " + delta + " | Direction and speed of fire: " + echo + " | Terrain: " + foxtrot + " | Number of endangered people: " + golf + " | Level of danger: " + hotel + ' | Action taken: ' + india + ' | Casualties: ' + juliet + ' | Best route to location: ' + kilo + ' | Other information: ' + lima + '\n';
    
    document.getElementById('output').value = output  + out;
    document.getElementById('bushfire_duff').value = '';
    document.getElementById('bushfire_callsign').value = '';
    document.getElementById('bushfire_grid').value = '';
    document.getElementById('bushfire_evac').value = '';
    document.getElementById('bushfire_extent').value = '';
    document.getElementById('bushfire_direcspeed').value = '';
    document.getElementById('bushfire_terrain').value = '';
    document.getElementById('bushfire_numberperson').value = '';
    document.getElementById('bushfire_danger').value = '';
    document.getElementById('bushfire_actiontaken').value = '';
    document.getElementById('bushfire_casualties').value = '';
    document.getElementById('bushfire_route').value = '';
    document.getElementById('bushfire_info').value = '';
}
function noticas(){
    var duff = document.getElementById('noticas_duff').value,
        alpha = document.getElementById('noticas_callsign').value,
        bravo = document.getElementById('noticas_grid').value,
        charlie = document.getElementById('noticas_person').value,
        delta = document.getElementById('noticas_injury').value,
        echo = document.getElementById('noticas_place').value,
        foxtrot = document.getElementById('noticas_time').value,
        output = document.getElementById('output').value,
        time = new Date(),
        time = String(time),
        time = time.substring(0, 21),
        out = time + ' | NOTICAS | No Duff or exercise: ' + duff + " | Callsign: " + alpha + " | Location: " +  bravo + " | Person injured: " + charlie + " | Type of injury: " + delta + " | Place injured: " + echo + " | Time injured: " + foxtrot + '\n';
    document.getElementById('output').value = output  + out;
    document.getElementById('noticas_duff').value = '';
    document.getElementById('noticas_callsign').value = '';
    document.getElementById('noticas_grid').value = '';
    document.getElementById('noticas_person').value = '';
    document.getElementById('noticas_injury').value = '';
    document.getElementById('noticas_place').value = '';
    document.getElementById('noticas_time').value = '';
}
function flood(){
    var duff = document.getElementById('flood_duff').value,
        alpha = document.getElementById('flood_callsign').value,
        bravo = document.getElementById('flood_grid').value,
        charlie = document.getElementById('flood_evac').value,
        delta = document.getElementById('flood_extent').value,
        echo = document.getElementById('flood_direcspeed').value,
        foxtrot = document.getElementById('flood_terrain').value,
        golf = document.getElementById('flood_numberperson').value,
        hotel = document.getElementById('flood_route').value,
        india = document.getElementById('flood_actiontaken').value,
        juliet = document.getElementById('flood_casualties').value,
        kilo = document.getElementById('flood_comments').value,
        lima = document.getElementById('flood_info').value,
        output = document.getElementById('output').value,
        time = new Date(),
        time = String(time),
        time = time.substring(0, 21),
        out = time + ' | Flood | No Duff or exercise: ' + duff + " | Callsign: " + alpha + " | Location: " +  bravo + " | Evacuation required: " + charlie + " | Extent of flood: " + delta + " | Direction and speed of flood: " + echo + " | Terrain: " + foxtrot + " | Number of endangered people: " + golf + " | Best route to location: " + hotel + ' | Action taken: ' + india + ' | Casualties: ' + juliet + ' | Comments: ' + kilo + ' | Other information: ' + lima + '\n';
    
    document.getElementById('output').value = output  + out;
    document.getElementById('flood_duff').value = '';
    document.getElementById('flood_callsign').value = '';
    document.getElementById('flood_grid').value = '';
    document.getElementById('flood_evac').value = '';
    document.getElementById('flood_extent').value = '';
    document.getElementById('flood_direcspeed').value = '';
    document.getElementById('flood_terrain').value = '';
    document.getElementById('flood_numberperson').value = '';
    document.getElementById('flood_danger').value = '';
    document.getElementById('flood_actiontaken').value = '';
    document.getElementById('flood_casualties').value = '';
    document.getElementById('flood_route').value = '';
    document.getElementById('flood_info').value = '';
}