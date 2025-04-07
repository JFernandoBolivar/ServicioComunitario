
document.addEventListener("DOMContentLoaded", () => {

  const exit = document.getElementById("exit");


  if (exit) {
    exit.addEventListener("click", () => {
      const alertDiv = document.querySelector(".alert");
      if (alertDiv) {
        alertDiv.style.display = "none";
      }
    });
  }
});
