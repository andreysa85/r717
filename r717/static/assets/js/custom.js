
jQuery( document ).ready(function( $ ) {

//============= Додавання торвару до кошика ============================ 
function getCookie(c_name) {
    if (document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}
$('.btn_buy').on('click', function(){
    var product_id = $(this).attr('id_product');
    $.ajax({
        type : "POST",
        url : '/cart/ajax_cart_plus/'+ product_id+'/',
        data : {
            "product_id": product_id,
        },
        dataType : "json",
        success : function(data){
            $("#count_info").html(data['count']);
        },       
    });
});
$('.btn_buy').on('click', function(){

    var that = $(this).closest('.product-item').find('img');
    var product_id = $(this).attr('id_btn');
    var bascket = $(".basket");
    var w = that.width();
    that.clone()
    .css({'width' : w,
        'position' : 'absolute',
        'z-index' : '9999',
        top: that.offset().top,
        left:that.offset().left})
    .appendTo("body")
    .animate({opacity: 0.5,
        left: bascket.offset()['left'],
        top: bascket.offset()['top'],
        width: 20}, 1000, function() {  
            $(this).remove();
        });
});


//==================================================================


//============= Настройка слайдера SWAPER ============================ 
var swiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 0,
    // centeredSlides: true,
    autoplay: {
      delay: 2500,
      disableOnInteraction: false,
  },
  pagination: {
      el: ".swiper-pagination",
      clickable: true,
  },
  navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
  },
});
//==================================================================

// ==========Фильтрация продуктов==========
$('.filters ul li').click(function(){
    $('.filters ul li').removeClass('active');
    $(this).addClass('active');
    $('.accordion > li:eq(0) a').addClass('active').next().slideDown();
    $('.accordion a').click(function(j) {
        var dropDown = $(this).closest('li').find('.content');
        $(this).closest('.accordion').find('.content').not(dropDown).slideUp();
        if ($(this).hasClass('active')) {
            $(this).removeClass('active');
        } else {
            $(this).closest('.accordion').find('a.active').removeClass('active');
            $(this).addClass('active');
        }
        dropDown.stop(false, true).slideToggle();
        j.preventDefault();
    });
        // Иніціюємо Isotope
        var $grid = $('.grid').isotope({
          // опції
          itemSelector: ".all",
          percentPosition: true,
          layoutMode: 'fitRows'
      });
        // фільтруємо при натисканні на посилання
        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        });
    });
//==================================================================


// ========== Добавление всплывающего окна для подтверждения отправки письма==========
$("#send-mail").click(function(){
    $('#myModal').modal('show');
}); 
$('#send_mess').on('click', function () {
  var recipient_name = document.getElementById('recipient-name').value;
  var recipient_сontacts = document.getElementById('recipient-сontacts').value;
  var message_text = document.getElementById('message-text').value;
  $.ajax({
    url: '/tst', 
    dataType: 'json',
    data: {
        "recipient_name": recipient_name,
        "recipient_сontacts":recipient_сontacts, 
        "message_text":message_text
    },
    success: function(result){
        $('#myModal').modal('hide');
        $('#myModal_sucsesful').modal('show');
        window.location.reload();
    }
});
});
//==================================================================

//=============Зірковий рейтинг продукту============================ 
$(".rateyo").rateYo({
    starWidth: "20px",
    ratedFill: "#E74C3C",
}).on('rateyo.set',function(e, data){
    var product_id = $(this).attr('id_product');
    $.ajax({
        type : "get",
        url : "/rating_ajax/",
        data : {
            "rating" : data.rating,
            "product_id": product_id,
        },
        dataType : "json",
        success : function(data){
            var rating = data['res'];
            var votes = data['votes'];
            var div_id = document.getElementById(product_id);
            var close_rating = div_id.getElementsByClassName("rateyo"); 
            $(close_rating).rateYo("option", "readOnly", true);
            var set_votes = div_id.getElementsByClassName("vote");
            $(set_votes).empty();
            $(set_votes).append(votes);
        },       
    });
});

});
