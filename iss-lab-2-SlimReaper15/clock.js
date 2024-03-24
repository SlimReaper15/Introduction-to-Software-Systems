let is24 = true;

function toggleClockFormat() { // Keeps track of the toggle button, the onClick attribute of the button Toggle in the HTML file activates this function
    is24 = !(is24); // State of whether 24 hour clock should be displayed
    updateTimes();
}

function Hyderabad() {
    let hDate = new Date();
    let hHours = hDate.getHours();
    let hMinutes = hDate.getMinutes();
    let hSeconds = hDate.getSeconds();
    let hTime = document.getElementById("thyd"); // thyd is the identifier of Hyderabad clock

    if (!is24) {
        let ampm; // Shows AM or PM in 12 hour clock
        if (hHours >= 12)
            ampm = 'PM';
        else
            ampm = 'AM';

        if (hHours % 12 === 0)
            hHours = 12;
        else
            hHours = hHours % 12; // Converting 24 hour to 12 hour clokc


        hTime.textContent = zero(hHours) + ":" + zero(hMinutes) + ":" + zero(hSeconds) + " " + ampm; // Calling the zero function to pad zeroes

    }
    else
        hTime.textContent = zero(hHours) + ":" + zero(hMinutes) + ":" + zero(hSeconds);
}

function SanFrancisco() {
    let sfDate = new Date();
    let sfHours = (sfDate.getUTCHours() - 8 + 24) % 24; // Kobe Bryant numbers
    let sfMinutes = sfDate.getUTCMinutes();
    let sfSeconds = sfDate.getUTCSeconds();
    let sfTime = document.getElementById("tsfo");

    if (!is24) {
        let ampm;
        if (sfHours >= 12)
            ampm = 'PM';
        else
            ampm = 'AM';

        if (sfHours % 12 === 0)
            sfHours = 12;
        else
            sfHours = sfHours % 12;

        sfTime.textContent = zero(sfHours) + ":" + zero(sfMinutes) + ":" + zero(sfSeconds) + " " + ampm;

    }
    else
        sfTime.textContent = zero(sfHours) + ":" + zero(sfMinutes) + ":" + zero(sfSeconds);
}

function GMT() {
    let gmtDate = new Date();
    let gmtHours = gmtDate.getUTCHours();
    let gmtMinutes = gmtDate.getUTCMinutes();
    let gmtSeconds = gmtDate.getUTCSeconds();
    let gmtTime = document.getElementById("tgmt");

    if (!is24) {
        let ampm;
        if (gmtHours >= 12)
            ampm = 'PM';
        else
            ampm = 'AM';

        if (gmtHours % 12 === 0)
            gmtHours = 12;
        else
            gmtHours = gmtHours % 12;

        gmtTime.textContent = zero(gmtHours) + ":" + zero(gmtMinutes) + ":" + zero(gmtSeconds) + " " + ampm;

    }
    else
        gmtTime.textContent = zero(gmtHours) + ":" + zero(gmtMinutes) + ":" + zero(gmtSeconds);
}


function zero(value) {
    return (value < 10) ? '0' + value : value; // Adds a 0 before each of hours, minutes and seconds if they're less than 10 to avoid ugly times like 1:2:3
}

function updateTimes() {
    Hyderabad();
    GMT();
    SanFrancisco();
}

// updateTimes();
setInterval(updateTimes, 1000);