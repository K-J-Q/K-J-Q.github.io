$(function () {
    $("body").prepend("<div id='header'></div>");
    $("body").append("<div id='footer'></div>");
    $("#header").load("header.html");
    $("#footer").load("footer.html");
});

document.getElementById("footerLink").innerHTML = "The full URL of this page is:<br>" + window.location.href;