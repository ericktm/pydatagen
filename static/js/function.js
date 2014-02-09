$(document).ready(function () {

    $(document).ajaxStart(function () {
        console.log('Ajax Start!');
    }).ajaxStop(function () {
        console.log('Ajax Stop!');
    });

    $('.btn-edit').button({
        icons: {
            primary: "ui-icon-pencil"
        }
    });
    $('.btnsave').button({
        icons: {
            primary: "ui-icon-locked"
        }
    });

    $('.btn-edit').on('click', function () {
        var element = $(this);
        var id = element.attr('id');
    });


    $('form').on('submit', function (e) {
        e.preventDefault();
        var form = $(this);
        var dados = form.serialize();
        $.post(form.attr('action'), dados, function (retorno) {
            console.log(retorno);
        });
        console.log(dados);
    });

});