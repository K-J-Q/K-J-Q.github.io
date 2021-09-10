$(function () {
    $("body").prepend("<div id='header'></div>");
    $("body").append("<div id='footer'></div>");
    $("#header").load("header.html");
    $("#footer").load("footer.html");
    console.log("test");
});