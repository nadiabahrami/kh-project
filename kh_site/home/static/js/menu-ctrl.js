$('.navbar-toggle').on('click', function(){
    if ($('#nav-mobile').hasClass('mobile-down')) {
        console.log('going up')
        $('#nav-mobile').animate({
            top: -370
        }).removeClass('mobile-down')                
    } else {
        console.log('going down')
        $('#nav-mobile').animate({
            top: 80
        }).addClass('mobile-down')                                
    }
})