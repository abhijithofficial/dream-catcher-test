let signInForm = document.querySelector("#login_submit");

signInForm.addEventListener("submit", (e) => {
  e.preventDefault();
  let username = document.getElementById("signInInputEmail").value;
  let password = document.getElementById("signInInputPassword").value;
  fetch("http://" + window.location.host + "/api/login/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  })
    .then((response) => {
      if (response.status === 400) {
        return new Error();
      } else {
        return response.json();
      }
    })
    .then((data) => {
      if (data.success) {
        window.location.href = data.data.redirect;
      } else {
        alert("Wrong password");
      }
    })
    .catch(() => alert("Wrong email or password"));
});
