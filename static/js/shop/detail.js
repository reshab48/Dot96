$(document).ready(function(){$(".item:first").addClass("active");for(var t=$(".item").length,a=0;t>a;a++){var i=".pointers:eq("+a.toString()+")";$(i).attr("data-slide-to",a.toString())}$(".item-box").hover(function(){$(this).addClass("w3-card")},function(){$(this).removeClass("w3-card")})});