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

    $('.btn-menu-simple').button();

    $(document).ajaxStart(function () {
        debug('ajax start.');
        $.blockUI({
            title: 'Aguarde..',
            message: '<h1><img src="/static/img/loader.gif"/></h1>',
            theme: true,
            themedCSS: {
                margin: '0 auto',
                position: 'absolute',
                marginLeft: '50%',
                left: '-120px',
                width: '240px',
                padding: '5px'
            }
        });
    }).ajaxStop(function () {
        debug('ajax end.');
        updateScreen();
        setTimeout(function () {
            $.unblockUI();
        }, 500)
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
            console.log('load page: ' + href);
            $('#center').load(href);
        }
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
                message('Erro!', retorno.error);
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
                    message('Sucesso', retorno.message, 'success');
                    $('#' + update).trigger("reloadGrid");
                } else {
                    message('Sucesso', retorno.error);
                }
            });
        }
    });

    $('body').on('click', '.btn-trash', function (e) {
        e.preventDefault();
        $('#confirm').remove();

        var url = $(this).attr('data-url');
        var update = $(this).attr('data-update');


        var div = '<div id="confirm" class="hidden" title="Confirmar exclusão">' +
            '<span class="ui-icon ui-icon-help" style="float:left; margin:0 7px 50px 0;"></span>' +
            'Deseja inativar o registro?' +
            '</div>';

        $(div).appendTo('body');

        $(div).dialog({
            resizable: false,
            height: 180,
            modal: true,
            closeOnEscape: true,
            close: function (event, ui) {
                $('#confirm').remove();
            },
            buttons: {
                "Excluir registro": function () {
                    console.log(url);
                    if (url != '#') {
                        $.get(url, function (retorno) {
                            if (retorno.success == true) {
                                message('Sucesso', retorno.message, 'success');
                            } else {
                                message('Sucesso', retorno.error);
                            }
                            //reloading grid
                            $('#' + update).trigger("reloadGrid");
                        });
                    }
                    $(this).dialog("close");
                },
                Cancel: function () {
                    $(this).dialog("close");
                }
            }
        });
    });

    $(document).on('click', '.btn-clean', function (e) {
        var update = $(this).attr('data-update');

        $("#" + update).jqGrid('setGridParam', {postData: {}}).trigger('reloadGrid');

        message('Sucesso', 'Parâmetros de busca limpos!', 'success');
    });

    function updateScreen() {

        $('.accordion').accordion({
            collapsible: true
        });

        $('.btn-search').button({
            icons: {
                primary: 'ui-icon-search'
            }
        });

        $('.btn-field').button({
            icons: {
                primary: 'ui-icon-script'
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

        $('.btn-trash-icon').button({
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

        $('.btn-start').button({
            icons: {
                primary: 'ui-icon-play'
            }
        });

        $('.btn-files').button({
            icons: {
                primary: 'ui-icon-arrowthickstop-1-s'
            }
        });


    }
});