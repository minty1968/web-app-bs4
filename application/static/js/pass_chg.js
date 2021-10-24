var password = document.getElementById("password")
  , confirm = document.getElementById("confirm");

function validatePassword(){
  if(password.value != confirm.value) {
    confirm.setCustomValidity("Passwords Don't Match");
  } else {
    confirm.setCustomValidity('');
  }
}

password.onchange = validatePassword;
confirm.onkeyup = validatePassword;