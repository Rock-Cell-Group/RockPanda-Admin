document.addEventListener("DOMContentLoaded", function () {
    var buttons = document.querySelectorAll(".clickable_scuccess_button");
    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            document.getElementById("demo").innerHTML = "Hello World";
        });
        button.addEventListener("click", function () {
            document.getElementById("demo").innerHTML = "Good";
        });
    });
});


document.addEventListener("DOMContentLoaded", function () {
    var buttons = document.querySelectorAll(".clickable_failed_button");
    buttons.forEach(function (button) {
        button.addEventListener("click", function () {
            document.getElementById("demo").innerHTML = "Error";
        });
    });
});


