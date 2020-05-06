// Show form for new task
function new_task(event, input) {

    document.getElementById(input).style.display = "inline";
    document.getElementById('add').style.display = "none";
    document.getElementById('cancel').style.display = "inline";
}

// Hide form for new task
function cancel_new_task(event, input) {

    document.getElementById(input).style.display = "none";
    document.getElementById('add').style.display = "inline";
    document.getElementById('cancel').style.display = "none";
}

var date = document.getElementById('due-date');
date.onfocus = function (event) {
    this.type = 'datetime-local';
    this.focus();
}