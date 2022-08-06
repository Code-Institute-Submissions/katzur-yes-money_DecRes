const usernameField = document.querySelector("#usernameField");
const feedbackArea = document.querySelector(".invalid_feedback");
const emailField = document.querySelector("#emailField");
const EmailFeedbackArea = document.querySelector(".EmailFeedbackArea");
const passwordField = document.querySelector("#passwordField");
const usernameSuccessOutput = document.querySelector(".usernameSuccessOutput");
const checkbox = document.querySelector("#showPasswordToggle");
const submitButton = document.querySelector(".submit-btn")


checkbox.addEventListener("click", (e) => {
    if (e.target.checked) {
        checkboxDescription.textContent = "Show the password";
        passwordField.setAttribute("type", "text");
    } else {
        checkboxDescription.textContent = "Hide the password";
        passwordField.setAttribute("type", "password");
    }
});


emailField.addEventListener("keyup", (e) => {
    const emailVal = e.target.value;

    emailField.classList.remove("is-invalid");
    EmailFeedbackArea.style.display = "none";

    if (emailVal.lenght > 0) {
        fetch("/authentication/validate-email", {
                body: JSON.stringify({
                    email: emailVal
                }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                console.log("data", data);
                if (data.email_error) {
                    submitButton.disabled = true;
                    emailField.classList.add("is-invalid");
                    EmailFeedbackArea.style.display = "block";
                    EmailFeedbackArea.innerHTML = `<p>${data.email_error}</p>`;
                } else {
                    submitButton.removeAttribute("disabled");
                }
            });
    }
});


usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;

    usernameSuccessOutput.style.display = "block";
    usernameSuccessOutput.textContent = `Checking ${usernameVal}`;

    usernameField.classList.remove("is-invalid");
    feedbackArea.style.display = "none";

    if (usernameVal.lenght > 0) {
        fetch("/authentication/validate-username", {
                body: JSON.stringify({
                    username: usernameVal
                }),
                method: "POST",
            })
            .then((res) => res.json())
            .then((data) => {
                usernameSuccessOutput.style.display = "none";
                if (data.username_error) {
                    usernameField.classList.add("is-invalid");
                    feedbackArea.style.display = "block";
                    feedbackArea.innerHTML = `<p>${data.username_error}</p>`;
                    submitButton.disabled = true;
                } else {
                    submitButton.removeAttribute("disabled");
                }
            });
    }
});