$(document).ready(()=>{
    formInputs = document.getElementsByTagName('input')

    for (inp in formInputs){
        formInputs[inp].className += 'form-control'
    }

    formInputs[1].id = 'email'
    formInputs[1].placeholder = 'Email'
    formInputs[2].id = 'password'
    formInputs[2].placeholder = 'Password'

    formInputs[5].id = 'email'
    formInputs[5].placeholder = 'Email'
    formInputs[6].id = 'password'
    formInputs[6].placeholder = 'Password'

    console.log(formInputs)
})