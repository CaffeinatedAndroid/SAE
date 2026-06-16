// Variables and Data Types
let message = "Hello, JavaScript!";
console.log(message);
// Function Declaration
function greetUser() {
    alert("Welcome to JavaScript Fundamentals and Responsive Design!");
}
// Run after the page has loaded
document.addEventListener("DOMContentLoaded", function () {
    greetUser();
    // DOM Manipulation
    let button = document.getElementById("changeText");
    let text = document.getElementById("text");
    button.addEventListener("click", function () {
        text.textContent =
        "You clicked the button! JavaScript is working inside a responsive layout.";
    text.style.color = "blue";
    console.log("Button clicked successfully.");
    });
});
