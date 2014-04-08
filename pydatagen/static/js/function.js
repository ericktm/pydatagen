function debug(msg) {
    if (DEBUG) {
        console.log(msg);
    }
}

function message(title, content, type) {
    if (!type) {
        type = 'info';
    }
    $.jGrowl(content, {
        header: title
    });
}

$.jGrowl.defaults.closerTemplate = '<div>Fechar todas </div>';

$(document).ready(function () {
    $('.btn-menu').button({
        icons: {
            secondary: "ui-icon-triangle-1-s"
        }
    });

    $(document).ajaxStart(function () {
        debug('Iniciando requisição ajax.');
        $.blockUI({
            message: '<h1> Carregando... </h1>',
            css: {
                border: 'none',
                padding: '15px',
                backgroundColor: 'white',
                backgroundRepeat: 'no-repeat',
                backgroundImage: 'url("/static/img/loader.gif")',
                backgroundPosition: 'center',
                '-webkit-border-radius': '10px',
                '-moz-border-radius': '10px',
                opacity: .5,
                color: '#0073ea',
                paddingTop: '130px'
            }
        });
    }).ajaxStop(function () {
        debug('Requisição ajax finalizada!');
        updateScreen();
        setTimeout(function () {
            $.unblockUI();
        }, 1000)
    });


    $('.sub_menu ul li').mouseover(function () {
        $(this).addClass('ui-state-hover');
    });

    $('.sub_menu ul li').mouseout(function () {
        $(this).removeClass('ui-state-hover');
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

    $('.load').on('click', function (e) {
        e.preventDefault();
        var href = $(this).attr('href');
        if (href != '#') {
            $('#center *').remove();
            console.log('Carregando página ' + href);
            $('#center').load(href);
        }
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

    $(document).on('submit', '.form_post', function (e) {
        e.preventDefault();

        var url = $(this).attr('action');
        var update = $(this).attr('data-update');
        var close = $(this).attr('data-close');

        $.post(url, $(this).serialize(), function (retorno) {
            debug(retorno);
            if (retorno.success == true) {
                message('Sucesso', 'Registro salvo com sucesso', 'success');
                $('#' + update).trigger("reloadGrid");
                $('#' + close).remove();
            } else {
                message('Sucesso', 'Registro salvo com sucesso');
            }

        });

    });

    $(document).on('click', '.open', function (e) {
        e.preventDefault();

        var div = $(this).attr('data-div');
        var url = $(this).attr('data-url');

        if (url != '#') {
            $('#' + div).remove();
            $('<div id="' + div + '" class="hidden"></div>').appendTo('#center');

            $('#' + div).load(url);

            $('#' + div).dialog({
                title: $(this).attr('data-title'),
                height: $(this).attr('data-height'),
                width: $(this).attr('data-width'),
                modal: true,
                resizable: false
            });
        }


    });

    $(document).on('click', '.action', function (e) {
        e.preventDefault();

        var url = $(this).attr('data-url');
        var update = $(this).attr('data-update');


        if (url != '#') {
            $.get(url, function (retorno) {
                debug(retorno);
                if (retorno.success == true) {
                    message('Sucesso', 'Registro removido com sucesso', 'success');
                    $('#' + update).trigger("reloadGrid");
                } else {
                    message('Sucesso', retorno.error);
                }
            });
        }


    });

    function updateScreen() {

        debug('Atualizando tela');

        $('#accordion').accordion({
            collapsible: true
        });

        $('.btn-search').button({
            icons: {
                primary: 'ui-icon-search'
            }
        });

        $('.btn-add').button({
            icons: {
                primary: 'ui-icon-plus'
            }
        });


        $('.btn-edit').button({
            icons: {
                primary: 'ui-icon-pencil'
            }
        });

        $('.btn-trash').button({
            icons: {
                primary: 'ui-icon-trash'
            }
        });

        $('.btn-clean').button({
            icons: {
                primary: 'ui-icon-tag'
            }
        });

        $('.btn-table').button({
            icons: {
                primary: 'ui-icon-calculator'
            }
        });

        $('.btn-view').button({
            icons: {
                primary: 'ui-icon-search'
            }
        });

        $('.btn-save').button({
            icons: {
                primary: 'ui-icon-disk'
            }
        });
    }
});