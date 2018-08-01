
var introTagA =  document.getElementById("introTagA")
var introVideoTagA = document.getElementById("introVideoTagA")
var aboutMeTagA = document.getElementById("aboutMeTagA")

var hamburgerBar = document.getElementsByClassName("hamburgerBar");
var nav =   document.getElementsByTagName("nav");


function closeNav() {
  if (nav.classList) {
    nav.classList.remove("open");
    nav.classList.toggle("close");
  }
}

introTagA.addEventListener("click", function() {
  $("nav").toggleClass("close");
  $([document.documentElement, document.body]).animate({
    scrollTop: 0
}, 1000);
})

introVideoTagA.addEventListener("click", function() {
  $("nav").toggleClass("close");
  $([document.documentElement, document.body]).animate({
    scrollTop: $('#introductionVideo').offset().top-50
}, 1000);
})

 aboutMeTagA.addEventListener("click", function() {
  $("nav").toggleClass("close");
  $([document.documentElement, document.body]).animate({
    scrollTop: $('#aboutMe').offset().top
}, 1000);
})


$(".hamburgerBar").click(function(){
  $("nav").removeClass("close");
  $("nav").toggleClass("open");
});

var swiper = new Swiper('.swiper-container', {
  pagination: {
    el: '.swiper-pagination',
  },
});
