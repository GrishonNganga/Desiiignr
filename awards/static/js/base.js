function follow(user){
    let classes = user.toElement.className
    let user_form = classes.split(' ', 1)[0]
    let user_id = user_form.substring(6)

    let followForm = $('#'+user_form)

        $.ajax({
            'url': '/follow',
            'type': 'POST',
            'data': followForm.serialize(),
            'datatype': 'json',
            'success':(data)=>{
                if (data['success']){
                    $('.'+user_form).hide()
                    $('.user'+user_id).remove()
                    $('.following-hidden'+user_id).show()
                }else{
                }
                
            }
        })
}

function followSuggested(user){
    let classes = user.toElement.className
    let user_form = classes.split(' ', 1)[0]
    let user_id = user_form.substring(6)

    let followForm = $('#'+user_form)

        $.ajax({
            'url': '/follow',
            'type': 'POST',
            'data': followForm.serialize(),
            'datatype': 'json',
            'success':(data)=>{
                if (data['success']){
                    $('.user'+user_id).remove()
                    $('.liked-hidden'+post_id).show()
                    $('.'+likeFormId).hide()
                }else{
                }
                
            }
        })
}

function like_post(like){
    let likeClasses = like.toElement.className
    let likeFormId = likeClasses.split(' ', 1)[0]
    let post_id = likeFormId.substring(4)

    let likeForm = $('#'+ likeFormId)

    $.ajax({
        'url': '/like',
        'type': 'POST',
        'data': likeForm.serialize(),
        'datatype': 'json',
        'success':(data)=>{
            if (data['success']){
                $('.liked-hidden'+post_id).show()
                $('.'+likeFormId).hide()
            }else{
            }
            
        }
    })
    
}
