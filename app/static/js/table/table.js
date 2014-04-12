$(document).ready(function () {

    function actions(cellValue, options, rowObject) {
        var view = '<button class="btn-view mini open" title="Visualizar registro." data-url="/app/table/view/' + rowObject.id + '.html"></button>';
        var field = '<button class="btn-field mini open"' +
            'data-title="Campos da Tabela"' +
            'data-url="/app/field/' + rowObject.id + '.html"' +
            'data-div="window-field"' +
            'data-width="700"' +
            'data-height="500"' +
            '></button>';
        var edit = '<button class="btn-edit mini open"' +
            'data-div="dlg-table"' +
            'data-title="Editar Tabela"' +
            'data-width="500"' +
            'data-height="300"' +
            'data-url="/app/table/record/' + $('#project').val() + '/' + rowObject.id + '.html"></button>';
        var trash = '<button class="btn-trash mini action" data-update="tab_table" title="Excluir Tabela" data-url="/app/table/delete/' + rowObject.id + '.html"></button>';
        return field + edit + trash;
    }

    $("#tab_table").jqGrid({
        url: '/app/table/search.html',
        datatype: 'local',
        colNames: ['Ações', 'Código', 'Nome da Tabela', 'Ordem', 'Data criação', 'Data Edição'],
        colModel: [
            {name: 'actions', formatter: actions, align: "center", sortable: false},
            {name: 'id', index: 'id', width: 90, key: true},
            {name: 'name', index: 'name', width: 100},
            {name: 'order', index: 'order'},
            {name: 'created', index: 'created', width: 80, align: "center"},
            {name: 'edited', index: 'edited', width: 80, align: "center"}
        ],
        rowNum: 10,
        autowidth: true,
        height: '270',
        pager: '#pag_table',
        sortname: 'order',
        viewrecords: true,
        sortorder: "asc",
        hidegrid: false,
        caption: "Resultado da pesquisa",
        scrollOffset: 0,
        jsonReader: { repeatitems: false}
    });
    $("#tab_table").jqGrid('navGrid', '#pag_table', {edit: false, add: false, del: false, search: false});

    $(document).on('submit', '.busca_table', function (e) {
        e.preventDefault();
        $("#tab_table").jqGrid('setGridParam', {
            postData: {
                id: $('#codigo_tabela').val(),
                project: $('#project').val(),
                name: $('#nome_tabela').val()},
            datatype: 'json'
        }).trigger('reloadGrid');
    });

    $("#tab_table").jqGrid('setGridParam', {
        postData: {project: $('#project').val()},
        datatype: 'json'
    }).trigger('reloadGrid');


});
