$(document).ready(function () {
    $('.btn-menu').button({
        icons: {
            secondary: "ui-icon-triangle-1-s"
        }
    });

    $(document).ajaxStart(function () {
        console.log('Ajax Start!');
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
        console.log('Ajax Stop!');
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

});