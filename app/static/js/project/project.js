$(document).ready(function () {

    function actions(cellValue, options, rowObject) {
        var view = '<button class="btn-view mini open" title="Visualizar registro." data-url="/app/project/view/' + rowObject.id + '.html"></button>';
        var table = '<button class="btn-table mini open"' +
            'data-title="Tabelas do Projeto"' +
            'data-url="/app/table/' + rowObject.id + '.html"' +
            'data-div="window-table"' +
            'data-width="700"' +
            'data-height="500"' +
            '></button>';
        var edit = '<button class="btn-edit mini open"' +
            'data-div="dlg-project"' +
            'data-title="Editar Projeto"' +
            'data-width="500"' +
            'data-height="300"' +
            'data-url="/app/project/record/' + rowObject.id + '.html"></button>';
        var trash = '<button class="btn-trash mini action" data-update="tab_project" title="Excluir Projeto" data-url="/app/project/delete/' + rowObject.id + '.html"></button>';
        debug(rowObject.id)
        return view + table + edit + trash;
    }

    $("#tab_project").jqGrid({
        url: '/app/project/search.html',
        datatype: 'local',
        colNames: ['Ações', 'Código', 'Nome do Projeto', 'Data criação', 'Data Edição'],
        colModel: [
            {name: 'actions', width: 50, formatter: actions, align: "center", sortable: false},
            {name: 'id', index: 'id', width: 90, key: true},
            {name: 'name', index: 'name', width: 200},
            {name: 'created', index: 'created', width: 80, align: "center"},
            {name: 'edited', index: 'edited', width: 80, align: "center"}
        ],
        rowNum: 10,
        autowidth: true,
        rowList: [10, 15, 20],
        height: 'auto',
        minHeight: '270px',
        pager: '#pag_project',
        sortname: 'id',
        viewrecords: true,
        sortorder: "asc",
        hidegrid: false,
        caption: "Resultado da pesquisa",
        scrollOffset: 0,
        jsonReader: { repeatitems: false}
    });
    $("#tab_project").jqGrid('navGrid', '#pag_project', {edit: false, add: false, del: false, search: false});

    $(document).on('submit', '.busca_projeto', function (e) {
        e.preventDefault();
        $("#tab_project").jqGrid('setGridParam', {
            postData: {id: $('#codigo').val(), name: $('#nome').val()},
            datatype: 'json'
        }).trigger('reloadGrid');
    });
});
