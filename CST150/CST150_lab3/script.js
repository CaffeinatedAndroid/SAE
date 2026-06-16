// Variables and Data Types
let message = "Hello, JavaScript!";
console.log(message);

// Function Declaration
function greetUser() {
    alert("Welcome to JavaScript Fundamentals!");
}

// DOM Manipulation
let button = document.getElementById("changeText");
let text = document.getElementById("text");
button.addEventListener("click", function() {
    text.textContent = "You clicked the button!";
    text.style.color = "blue";
});


document.addEventListener("DOMContentLoaded", greetUser);
