/**
 * Created by Erick on 04/06/14.
 */

function message(title, content, type) {
    if (!type) {
        type = 'info';
    }
    $.jGrowl(content, {
        header: title
    });
}



$(document).ready(function () {

    $('#window').dialog({
        resizable: false,
        modal: true,
        closeOnEscape: false
    });

    $('#btn_login').button({
        icons: {
            secondary: "ui-icon-key"
        }
    });

    $(".ui-dialog-titlebar-close").hide();


    $('#form_login').on('submit', function (e) {
        e.preventDefault();
        var form = $(this);
        var dados = form.serialize();
        $.post(form.attr('action'), dados, function (retorno) {
            if (retorno.status == 'success') {
                window.location = "/";
            } else {
                message('Erro na autenticação', retorno.message, 'error');
            }
        });
        console.log(dados);
    });
});
