/**
 * Created by Erick on 04/06/14.
 */

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
});
