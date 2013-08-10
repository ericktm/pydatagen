$(document).ready(function () {
    $(function () {
        $('#toolbar a').button();
    });
    $('#create-conection').button();
    $('.btnsave').button({
        icons: {
            primary: "ui-icon-locked"
        }
    });
    $('#create-conection').on('click', function () {
        $('.window').dialog({
            modal: true
        });
    });
    $('form').on('submit',function(e){
        e.preventDefault();
        var form = $(this);
        var dados = form.serialize();
        $.post(form.attr('action'),dados,function(retorno){
            console.log(retorno);
        });
        console.log(dados);
    });
});