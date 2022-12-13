function hideobj(id) {
    $('#' + id).hide()
}
function fadeobj(id,duration) {
    $('#' + id).fadeOut(duration)
}
function buttonanim(id,op) {
    $('#'+id).animate({
        opacity: op
    },200)
}
