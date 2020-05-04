// Show form for new task
function new_task(event, input) {

    document.getElementById(input).style.display = "inline";
}

var date = document.getElementById('due-date');
date.onfocus = function (event) {
    this.type = 'datetime-local';
    this.focus();
}