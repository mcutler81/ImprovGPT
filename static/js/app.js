document.addEventListener("DOMContentLoaded", function() {

    const form = document.getElementById("performance-form");
    const output = document.getElementById("output");
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
      
      const scene = document.getElementById("scene").value;
      const director_notes = document.getElementById("director_notes").value;
  
      fetch("http://localhost:5000/perform", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ scene, director_notes }),
      })
      .then(response => response.json())
      .then(data => {
        let performanceOutput = "";
        for (const [key, value] of Object.entries(data)) {
          performanceOutput += `${key}: ${value}\n`;
        }
        output.textContent = performanceOutput;
      })
      .catch((error) => {
        console.error("Error:", error);
        output.textContent = `Error: ${error}`;
      });
    });
  });
  