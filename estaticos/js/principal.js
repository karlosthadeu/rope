/* Efeito parallax */
$(document).ready(function(){
    $('.parallax').each(function(){
        var $obj = $(this);     
        $(window).scroll(function() {
            var yPos =  - ( $(window).scrollTop()  / 5 ); 
            var bgpos = '0% '+ yPos + 'px';
            $obj.css({'background-position': bgpos});
        });
    }); 
});
