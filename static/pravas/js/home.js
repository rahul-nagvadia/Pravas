const button1 = document.getElementById("button1");
const button2 = document.getElementById("button2");
const button3 = document.getElementById("button3");
const button4 = document.getElementById("button4");
const div1 = document.getElementById("div1");
const div2 = document.getElementById("div2");
const div3 = document.getElementById("div3");
const div4 = document.getElementById("div4");
const bus = document.getElementById("bus")
const train = document.getElementById("train")
const flight = document.getElementById("flight")

button1.addEventListener("click", () => {
  div1.style.display = "block";
  bus.style.display = "block";
  train.style.display = "none";
  flight.style.display = "none";
  div2.style.display = "none";
  div3.style.display = "none";
  div4.style.display = "none";
});

button2.addEventListener("click", () => {
  div1.style.display = "none";
  div2.style.display = "block";
  train.style.display = "block";
  bus.style.display = "none";
  flight.style.display = "none";
  div3.style.display = "none";
  div4.style.display = "none";
});

button3.addEventListener("click", () => {
  div1.style.display = "none";
  div2.style.display = "none";
  flight.style.display = "block";
  bus.style.display = "none";
  train.style.display = "none";
  div3.style.display = "block";
  div4.style.display = "none";
});

button4.addEventListener("click", () => {
  div1.style.display = "none";
  div2.style.display = "none";
  div3.style.display = "none";
  div4.style.display = "block";
  flight.style.display = "none";
  bus.style.display = "none";
  train.style.display = "none";
});

