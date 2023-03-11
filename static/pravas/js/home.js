const button1 = document.getElementById("button1");
      const button2 = document.getElementById("button2");
      const button3 = document.getElementById("button3");
      const div1 = document.getElementById("div1");
      const div2 = document.getElementById("div2");
      const div3 = document.getElementById("div3");

      button1.addEventListener("click", () => {
        div1.style.display = "block";
        div2.style.display = "none";
        div3.style.display = "none";
      });

      button2.addEventListener("click", () => {
        div1.style.display = "none";
        div2.style.display = "block";
        div3.style.display = "none";
      });

      button3.addEventListener("click", () => {
        div1.style.display = "none";
        div2.style.display = "none";
        div3.style.display = "block";
      });

      const today = new Date().toISOString().split("T")[0];
      const sourceField = document.getElementsByName("source")[0];
      const destinationField = document.getElementsByName("destination")[0];
      const dateField = document.getElementsByName("date_booked")[0];

      function validateForm() {
        if (sourceField.value === destinationField.value) {
          alert("Source and Destination cannot be the same");
          return false;
        }
        if (dateField.value < today) {
          alert("Date should be greater than or equal to today");
          return false;
        }
        return true;
      }