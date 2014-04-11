function printoutput(){
    document.getElementById('bigthing').style.display = 'none';
    document.getElementById('printtext').style.display = 'block';
    var content = document.getElementById('output').value,
        content = content.replace(/\n/gi, '<br>')
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
    document.getElementById('contact_callsign').value ='';
    document.getElementById('contact_grid').value = '';
    document.getElementById('contact_units').value = '';
    document.getElementById('contact_success').value = '';
    document.getElementById('contact_objective').value = '';
};