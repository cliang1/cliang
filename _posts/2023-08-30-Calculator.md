---
toc: true
comments: false
layout: post
title: Calculator
description: A calculator  
type: hacks
courses: { compsci: {week: 2} }
---


<!--
Hack 0: Right justify result
Hack 1: Test conditions on small, big, and decimal numbers, report on findings. Fix issues.
Hack 2: Add the common math operation that is missing from calculator
Hack 3: Implement 1 number operation (ie SQRT)
-->


<!--
HTML implementation of the calculator.
-->


{% include nav_home.html %}


<!--
    Style and Action are aligned with HRML class definitions
    style.css contains the majority of style definitions (number, operation, clear, and equals)
    - The div calculator-container sets 4 elements to a row
    Background is credited to Vanta JS and is implemented at the bottom of this page
-->
<style>
  .calculator-output {
    /* calulator output
      top bar shows the results of the calculator;
      result to take up the entirety of the first row;
      span defines 4 columns and 1 row
    */
    grid-column: span 4;
    grid-row: span 1;
 
    border-radius: 10px;
    padding: 0.25em;
    font-size: 20px;
    border: 5px solid black;
 
    display: flex;
    align-items: center;
  }


  /* Added style for the calculation history list */
  #history-list {
    display: none; /* Initially hide the history list */
  }


  /* Added style to make the history list visible when the button is clicked */
  #history-list.visible {
    display: block;
  }
</style>


<!-- Add a container for the animation -->
<div id="animation">
  <div class="calculator-container">
    <!-- Add a container for the calculation history -->
    <ul id="history-list"></ul>
    <div class="calculation-history">
      <h2>Calculation History</h2>
      <button id="show-history">Show History</button>
    </div>
    <!--result-->
    <div class="calculator-output" id="output">0</div>
    <!--row 1-->
    <div class="calculator-number">1</div>
    <div class="calculator-number">2</div>
    <div class="calculator-number">3</div>
    <div class="calculator-operation">+</div>
    <!--row 2-->
    <div class="calculator-number">4</div>
    <div class="calculator-number">5</div>
    <div class="calculator-number">6</div>
    <div class="calculator-operation">-</div>
    <!--row 3-->
    <div class="calculator-number">7</div>
    <div class="calculator-number">8</div>
    <div class="calculator-number">9</div>
    <div class="calculator-operation">*</div>
    <!--row 4-->
    <div class="calculator-clear">A/C</div>
    <div class="calculator-number">0</div>
    <div class="calculator-number">.</div>
    <div class="calculator-equals">=</div>
  </div>
</div>


<!-- JavaScript (JS) implementation of the calculator. -->
<script>
// initialize important variables to manage calculations
var firstNumber = null;
var operator = null;
var nextReady = true;
// Initialize the calculation history array
var calculationHistory = [];


// Function to update and display the calculation history
function updateHistory() {
  const historyList = document.getElementById("history-list");
  historyList.innerHTML = "";
  calculationHistory.forEach((calculation, index) => {
    const listItem = document.createElement("li");
    listItem.textContent = `Calculation ${index + 1}: ${calculation}`;
    historyList.appendChild(listItem);
  });
}


// Add a button click event listener to show the history
const showHistoryButton = document.getElementById("show-history");
showHistoryButton.addEventListener("click", () => {
  const historyList = document.getElementById("history-list");
  historyList.classList.toggle("visible"); // Toggle visibility of the history list
});


// Modify the 'equal' function to add calculations to the history
function equal() {
  if (firstNumber !== null) {
    const result = calculate(firstNumber, parseFloat(output.innerHTML));
    calculationHistory.push(`${firstNumber} ${operator} ${output.innerHTML} = ${result}`);
    updateHistory();
    firstNumber = result;
    output.innerHTML = result.toString();
    nextReady = true;
  }
}


// Modify the 'clearCalc' function to clear the history as well
function clearCalc() {
  firstNumber = null;
  output.innerHTML = "0";
  nextReady = true;
  calculationHistory = [];
  updateHistory();
}


// build objects containing key elements
const output = document.getElementById("output");
const numbers = document.querySelectorAll(".calculator-number");
const operations = document.querySelectorAll(".calculator-operation");
const clear = document.querySelectorAll(".calculator-clear");
const equals = document.querySelectorAll(".calculator-equals");


// Number buttons listener
numbers.forEach(button => {
  button.addEventListener("click", function() {
    number(button.textContent);
  });
});


// Number action
function number(value) {
  if (value != ".") {
    if (nextReady == true) {
      output.innerHTML = value;
      if (value != "0") {
        nextReady = false;
      }
    } else {
      output.innerHTML = output.innerHTML + value;
    }
  } else {
    if (output.innerHTML.indexOf(".") == -1) {
      output.innerHTML = output.innerHTML + value;
      nextReady = false;
    }
  }
}


// Operation buttons listener
operations.forEach(button => {
  button.addEventListener("click", function() {
    operation(button.textContent);
  });
});


// Operator action
function operation(choice) {
  if (firstNumber == null) {
    firstNumber = parseFloat(output.innerHTML);
    nextReady = true;
    operator = choice;
    return;
  }
  firstNumber = calculate(firstNumber, parseFloat(output.innerHTML));
  operator = choice;
  output.innerHTML = firstNumber.toString();
  nextReady = true;
}


// Calculator
function calculate(first, second) {
  let result = 0;
  switch (operator) {
    case "+":
      result = first + second;
      break;
    case "-":
      result = first - second;
      break;
    case "*":
      result = first * second;
      break;
    case "/":
      result = first / second;
      break;
    default:
      break;
  }
  return result;
}


// Equals button listener
equals.forEach(button => {
  button.addEventListener("click", function() {
    equal();
  });
});


// Equal action
function equal() {
  firstNumber = calculate(firstNumber, parseFloat(output.innerHTML));
  output.innerHTML = firstNumber.toString();
  nextReady = true;
}


// Clear button listener
clear.forEach(button => {
  button.addEventListener("click", function() {
    clearCalc();
  });
});


// A/C action
function clearCalc() {
  firstNumber = null;
  output.innerHTML = "0";
  nextReady = true;
}
</script>


<!--
Vanta animations just for fun, load JS onto the page
-->
<script src="/teacher/assets/js/three.r119.min.js"></script>
<script src="/teacher/assets/js/vanta.halo.min.js"></script>
<script src="/teacher/assets/js/vanta.birds.min.js"></
