function follow(user){
    let classes = user.toElement.className
    let user_form = classes.split(' ', 1)[0]
    console.log(user_form)
    let user_id = user_form.substring(6)

    let followForm = $('#'+user_form)
        console.log(followForm)

        $.ajax({
            'url': '/follow',
            'type': 'POST',
            'data': followForm.serialize(),
            'datatype': 'json',
            'success':(data)=>{
                if (data['success']){
                    console.log(data['success'])
                    $('.'+user_form).hide()
                    $('.following-hidden'+user_id).show()
                }else{
                    console.log(data['fail'])
                }
                
            }
        })
}