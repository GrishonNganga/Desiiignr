$(document).ready(()=>{
    formInputs = document.getElementsByTagName('input')

    for (inp in formInputs){
        formInputs[inp].className += 'form-control'
    }

    formInputs[1].id = 'username'
    formInputs[1].placeholder = 'Username'    
    formInputs[2].id = 'email'
    formInputs[2].placeholder = 'Email'
    formInputs[3].id = 'password1'
    formInputs[3].placeholder = 'Password'
    formInputs[4].id = 'password2'
    formInputs[4].placeholder = 'Confirm Password'

    formInputs[6].id = 'username'
    formInputs[6].placeholder = 'Username'    
    formInputs[7].id = 'email'
    formInputs[7].placeholder = 'Email'
    formInputs[8].id = 'password1'
    formInputs[8].placeholder = 'Password'
    formInputs[9].id = 'password2'
    formInputs[9].placeholder = 'Confirm Password'
    console.log(formInputs)
})