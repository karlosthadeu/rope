/* Barra lateral -------------------------------------------- início */

let lateral_exposta = true;
let lateral = $('#barra');
let content = $('#content');

// $('#btn-lateral').click(e => {
//     if(lateral_exposta){
//         lateral.removeClass('col-md-3');
//         content.removeClass('col-md-9');
//         content.addClass('col-md-12');
//         lateral_exposta = false; 
//     }
//     else{
//         lateral.addClass('col-md-3');
//         content.removeClass('col-md-12');
//         content.addClass('col-md-9');
//         lateral_exposta = true;
//     }
// });



/* Efeito parallax */
$(document).ready(function(){
    $('.parallax').each(function(){
        var $obj = $(this);     
        $(window).scroll(function() {
            var yPos =  - ( $(window).scrollTop()  / 2.5 ); 
            var bgpos = '0% '+ yPos + 'px';
            $obj.css({'background-position': bgpos});
        });
    }); 
});
