$(document).ready(()=>{
    $('.message_bubble').click(()=>{
        $('#comment').toggle()
        $('.post-btn').toggle()
    })
})

function comment(form, post){
    console.log(form)
    console.log(post)
}