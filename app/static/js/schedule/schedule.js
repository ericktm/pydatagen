$(document).ready(function () {

    function file_actions(cellValue, options, rowObject) {

        var edit = '<button class="btn-edit mini open"' +
            'data-div="dlg-table"' +
            'data-title="Opções de geração"' +
            'data-width="500"' +
            'data-height="160"' +
            'data-url="/app/project/record/' + rowObject.id + '.html"></button>';
        var trash = '<button class="btn-trash mini" data-update="tab_project" title="Excluir Projeto" data-url="/app/project/delete/' + rowObject.id + '.html"></button>';

        return edit + trash;
    }

    $("#tab_schedules").jqGrid({
        url: '/app/schedule/search.html',
        datatype: 'local',
        colNames: ['Ações', 'Ordem', 'Tabela', 'Quantidade de Registros'],

        colModel: [
            {name: 'actions', width: 50, formatter: file_actions, align: "center", sortable: false},
            {name: 'order', index: 'id', width: 50, align: "center"},
            {name: 'table', index: 'created', width: 80, align: "center"},
            {name: 'quantity', index: 'quantity', align: "center", width: 90}

        ],
        rowNum: 10,
        autowidth: true,
        rowList: [10],
        height: '270px',
        pager: '#pag_schedules',
        sortname: 'id',
        sortorder: "desc",
        hidegrid: false,
        caption: "Arquivos gerados no Projeto",
        scrollOffset: 0
    });
    $("#tab_schedules").jqGrid('navGrid', '#pag_schedules', {edit: false, add: false, del: false, search: false});

    $("#tab_schedules").jqGrid('setGridParam', {
        postData: {project: $('#project_id').val()},
        datatype: 'json'
    }).trigger('reloadGrid');
});