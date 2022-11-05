// Sign-up validations

function validateForm(){
    let usern = document.forms["myForm"]["username"].value;
    let eml = document.forms["myForm"]["email"].value;
    let passw = document.forms["myForm"]["pswd"].value;
    let cpassw = document.forms["myForm"]["cnpswd"].value;
    let rem = document.forms["myForm"]["remember"].value;

    if (usern == "") {
        alert("Name must be filled out");
        return false;
    }

    else if(eml == ""){
        alert("Email must be filled out");
        return false;
    }

    else if(passw == ""){
        alert("Password must be filled out");
        return false;
    }

    else if(cpassw = ""){
        alert("Confirm your password");
        return false;
    }

    else if(passw != cpassw){
        alert("Does not match the password");
        return false;
    }
    
}