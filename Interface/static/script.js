// Sign-up validations

const form = document.getElementById('form');
const username = document.getElementById('username');
const email = document.getElementById('email');
const password = document.getElementById('password');
const confirm_password = document.getElementById('confirm_password');

form.addEventListener('submit', e =>{
    e.preventDefault();

    validateInputs();
});


const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success');
};

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const validateInputs = () => {
    const usernameValue = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();
    const confirm_passwordValue = confirm_password.value.trim();

    if (usernameValue === null || usernameValue === "") {
        setError(username, 'Username is required');
    alert('Wueh')

    } else {
        setSuccess(username);
    }

    if (emailValue === null || emailValue === "") {
        setError(email, 'Email is required');
    } else {
        setSuccess(email);
    }

    if (passwordValue === null || passwordValue === "") {
        setError(email, 'Password is required');
    } else if(passwordValue < 8){
        setError(passwordValue, 'Password must be at least 8 character');
    } else {
        setSuccess(passwordValue);
    }

    if (confirm_passwordValue === null || confirm_passwordValue === "") {
        setError(email, 'Please confirm your password');
    } else if(confirm_passwordValue != passwordValue){
        setError(confirm_passwordValue, 'Passwords doesn\'t match');
    } else {
        setSuccess(confirm_passwordValue);
    }
};

