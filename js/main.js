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

var coll = document.getElementsByClassName("collapsible");
var i;
function lod() {
    for (i = 0; i < coll.length; i++) {
    coll[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var content = this.nextElementSibling;
        if (content.style.display === "block") {
        content.style.display = "none";
        } else {
        content.style.display = "block";
        }
    });
}}