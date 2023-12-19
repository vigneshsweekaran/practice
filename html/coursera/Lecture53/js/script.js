// DOM manipulation
// console.log(document.getElementById("title"));
// console.log(document instanceof HTMLDocument);

function sayHello() {
  var name = document.getElementById("name").value
  var message = "Hello " + name + "!!!"
  document.getElementById("content").textContent = message

  if (name === "student") {
    var title = document.querySelector("#title").textContent
    document.querySelector("#title").textContent = title += " - Welcome Student !!!!"
  }
}