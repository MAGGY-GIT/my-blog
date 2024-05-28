//this function is to set a specific timer for the messages
//the variable called will display nothing after the set time below

var message_timeout = document.getElementById("message-timer");

setTimeout(function()
{
    message_timeout.style.display = "none";
   

}, 3000);

