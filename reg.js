function validateForm() {
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const message = document.getElementById('passwordMessage');

    if (password !== confirmPassword) {
        message.innerText = "Passwords do not match";
        return false;
    }
    message.innerText = "";

    if (!validateCaptcha()) {
        return false;
    }

    return true;
}

function validateCaptcha() {
    const userAnswer = parseInt(document.getElementById("captchaAnswer").value);
    if (userAnswer !== correctAnswer) {
        alert("Incorrect CAPTCHA answer. Please try again.");
        return false;
    }
    return true;
}

const num1 = Math.floor(Math.random() * 10) + 1;
const num2 = Math.floor(Math.random() * 10) + 1;
const correctAnswer = num1 + num2;

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("captchaQuestion").innerText = `${num1} + ${num2} = ?`;
});

async function submitForm(event) {
    event.preventDefault();

    if (validateForm()) {
        const formData = {
            email: document.getElementById('email').value,
            phone: document.getElementById('phone').value,
            username: document.getElementById('username').value,
            dob: document.getElementById('dob').value,
            password: document.getElementById('password').value,
        };

        console.log("Form Data:", formData);  // Log the form data for debugging

        try {
            const response = await fetch('{% url "register_user" %}', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData),
            });

            if (response.ok) {
                alert('Registration successful!');
                window.location.href = '{% url "success" %}';
            } else {
                const errorMessage = await response.text();
                console.error("Error Message:", errorMessage);  // Log error message
                alert('Registration failed: ' + errorMessage);
            }
        } catch (error) {
            console.error("Fetch Error:", error.message);  // Log fetch error
            alert('An error occurred: ' + error.message);
        }
    }
}

