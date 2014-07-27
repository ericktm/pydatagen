$(document).ready(function () {

    function actions(cellValue, options, rowObject) {
        var view = '<button class="btn-view mini open" title="Visualizar registro." data-url="/app/field/view/' + rowObject.id + '.html"></button>';
        var edit = '<button class="btn-edit mini open"' +
            'data-div="dlg-field"' +
            'data-title="Editar Campo"' +
            'data-width="600"' +
            'data-height="600"' +
            'data-url="/app/field/record/' + $('#table').val() + '/' + rowObject.id + '.html"></button>';
        var trash = '<button class="btn-trash mini" data-update="tab_field" title="Excluir Campo" data-url="/app/field/delete/' + rowObject.id + '.html"></button>';
        return edit + trash;
    }

    $("#tab_field").jqGrid({
        url: '/app/field/search.html',
        datatype: 'local',
        colNames: ['Ações', 'Código', 'Nome', 'Tipo' , 'Preencher' , 'Data criação', 'Data Edição'],
        colModel: [
            {name: 'actions', formatter: actions, align: "center", sorfield: false},
            {name: 'id', index: 'id', width: 90, key: true},
            {name: 'name', index: 'name', width: 100},
            {name: 'type', index: 'type'},
            {name: 'insert', index: 'insert'},
            {name: 'created', index: 'created', width: 80, align: "center"},
            {name: 'edited', index: 'edited', width: 80, align: "center"}
        ],
        rowNum: 10,
        autowidth: true,
        height: '270',
        pager: '#pag_field',
        sortname: 'id',
        viewrecords: true,
        sortorder: "asc",
        hidegrid: false,
        caption: "Resultado da pesquisa",
        scrollOffset: 0,
        jsonReader: { repeatitems: false}
    });
    $("#tab_field").jqGrid('navGrid', '#pag_field', {edit: false, add: false, del: false, search: false});

    $(document).on('submit', '.busca_field', function (e) {
        e.preventDefault();
        $("#tab_field").jqGrid('setGridParam', {
            postData: {
                id: $('#codigo_campo').val(),
                name: $('#nome_campo').val()},
            datatype: 'json'
        }).trigger('reloadGrid');
    });

    $("#tab_field").jqGrid('setGridParam', {
        postData: {table: $('#table').val()},
        datatype: 'json'
    }).trigger('reloadGrid');


});
