$(document).ready(()=>{
    $('.message_bubble').click(()=>{
        $('#comment').toggle()
        $('.post-btn').toggle()
    })
})

function comment(form, post){
    form = $('#'+form)
    
    $.ajax({
        'url': '/comment',
        'type': 'POST',
        'data': form.serialize(),
        'success':(data)=>{
            if (data['success']){
                const commentMade = data['comment']
                console.log(commentMade)
                if (commentMade['image']){
                    $('.comments-section-lg').append(
                        `<div class="profile">
                        <div class="profile-photo up-tad">
                            <div class="row">
                                <div class="col-2">
                                    <a href="/profile">
                                        <img src="${commentMade['image']}" alt="">
                                    </a>
                                </div>
                                
                                <div class="col mt-3">
                                    ${commentMade['user']}  ${commentMade['comment']}
                                    
                                </div>
                            </div>
                        </div>
                    </div> `
                    )
                }else{
                    $('.comments-section-lg').append(
                        `<div class="profile">
                        <div class="profile-photo up-tad">
                            <div class="row">
                                <div class="col-2">
                                    <a href="/profile">
                                        <span class="material-icons profile-icon">account_circle</span>
                                    </a>
                                </div>
                                
                                <div class="col mt-3">
                                    ${commentMade['user']}  ${commentMade['comment']}
                                    
                                </div>
                            </div>
                        </div>
                    </div> `
                    )
                    
                }
                
            }else{
                console.log(data['fail'])
            }
            
        }
    })
}