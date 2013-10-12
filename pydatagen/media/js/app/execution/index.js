$(document).ready(function(){
       $('#btn-execute').button();

    $('#btn-execute').on('click',function(){
        $.get('#',function(retorno){
           console.log(retorno);
        });
    });
});