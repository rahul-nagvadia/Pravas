window.addEventListener("load", function () {
  var inputs = document.querySelectorAll(
    "input[type=text], input[type=password]"
  );
  for (i = 0; i < inputs.length; i++) {
    var inputEl = inputs[i];
    if (inputEl.value.trim() !== "") {
      inputEl.parentNode.classList.add("input--filled");
    }
    inputEl.addEventListener("focus", onFocus);
    inputEl.addEventListener("blur", onBlur);
  }

  function onFocus(ev) {
    ev.target.parentNode.classList.add("inputs--filled");
  }

  function onBlur(ev) {
    if (ev.target.value.trim() === "") {
      ev.target.parentNode.classList.remove("inputs--filled");
    }
  }
});
