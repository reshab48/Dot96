$(document).ready(function(){var t=!1;$(".row.list-group-item").hover(function(){t=$(this).hasClass("item-active"),0==t&&$(this).addClass("item-active")},function(){0==t&&$(this).removeClass("item-active")}),$(".row.list-group-item").click(function(){window.location.href=$(this).find("a").attr("data-href")})});