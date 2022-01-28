// ---------Responsive-navbar-active-animation-----------
function prettynav1(){
  $("#navbarSupportedContent").on("click","li",function(e){
    $('#navbarSupportedContent ul li').removeClass("active");
    $(this).addClass('active');
  });
}
$(document).ready(function(){
  setTimeout(function(){ prettynav1(); });
});
$(window).on('resize', function(){
  setTimeout(function(){ prettynav1(); });
});
$(".navbar-toggler").click(function(){
  setTimeout(function(){ prettynav1(); });
});


function prettynav(){
  var tabsNewAnim = $('#complexnavbarSupportedContent');
  var selectorNewAnim = $('#complexnavbarSupportedContent').find('li').length;
  var activeItemNewAnim = tabsNewAnim.find('.active');
  var activeWidthNewAnimHeight = activeItemNewAnim.innerHeight();
  var activeWidthNewAnimWidth = activeItemNewAnim.innerWidth();
  var itemPosNewAnimTop = activeItemNewAnim.position();
  var itemPosNewAnimLeft = activeItemNewAnim.position();
  $(".hori-selector").css({
    "top":itemPosNewAnimTop.top + "px", 
    "left":itemPosNewAnimLeft.left + "px",
    "height": activeWidthNewAnimHeight + "px",
    "width": activeWidthNewAnimWidth + "px"
  });
  $("#complexnavbarSupportedContent").on("click","li",function(e){
    $('#complexnavbarSupportedContent ul li').removeClass("active");
    $(this).addClass('active');
    var activeWidthNewAnimHeight = $(this).innerHeight();
    var activeWidthNewAnimWidth = $(this).innerWidth();
    var itemPosNewAnimTop = $(this).position();
    var itemPosNewAnimLeft = $(this).position();
    $(".hori-selector").css({
      "top":itemPosNewAnimTop.top + "px", 
      "left":itemPosNewAnimLeft.left + "px",
      "height": activeWidthNewAnimHeight + "px",
      "width": activeWidthNewAnimWidth + "px"
    });
  });
}
$(document).ready(function(){
  setTimeout(function(){ prettynav(); });
});
$(window).on('resize', function(){
  setTimeout(function(){ prettynav(); }, 50);
});
$(".navbar-toggler").click(function(){
  setTimeout(function(){ prettynav(); });
});
