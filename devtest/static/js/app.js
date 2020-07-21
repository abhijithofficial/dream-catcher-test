let signUpForm = document.querySelector("#signup_submit");
signUpForm.addEventListener("submit", (e) => {
  e.preventDefault();
  let username = document.getElementById("signUpUserName").value;
  let password = document.getElementById("signUpInputPassword1").value;
  let password_two = document.getElementById("signUpInputPassword2").value;
  let email = document.getElementById("signUpInputEmail").value;
  let firstname = document.getElementById("signUpInputFname").value;
  let lastname = document.getElementById("signUpInputLname").value;
  let phone = document.getElementById("signUpInputPhone").value;
  let address = document.getElementById("signUpInputAddress").value;

  if (password !== password_two) {
    return alert("Confirm Password Does Not Match");
  }
  fetch("http://localhost:8000/api/register/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      email,
      password,
      firstname,
      lastname,
      phone,
      address,
    }),
  })
    .then((response) => response.text())
    .then((data) => alert(data));
});
