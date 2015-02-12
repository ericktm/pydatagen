$(document).ready(function () {

    function file_actions(cellValue, options, rowObject) {

        var files = 'Sem arquivos.';

        if (rowObject.status == 'Concluído' && rowObject.quantity > 0) {
            files = '<a class="btn-files mini" ' +
            'title="Arquivos Gerados"' +
            'target="_blank" ' +
            'href="/media/project_files/' + rowObject.id + '.sql"' +
            'disabled="true"></a>';
        }

        return files;
    }

    $("#tab_files").jqGrid({
        url: '/app/project/files/search.html',
        datatype: 'local',
        colNames: ['Baixar', 'Código', 'Data criação', 'Situação', 'Quant. Gerada', 'Início', 'Fim', 'Log'],

        colModel: [
            {name: 'actions', width: 100, formatter: file_actions, align: "center", sortable: false},
            {name: 'id', index: 'id', width: 50, align: "center", key: true},
            {name: 'created', index: 'created', width: 80, align: "center"},
            {name: 'status', index: 'status', align: "left", width: 90},
            {name: 'quantity', index: 'quantity', align: "center", width: 90},
            {name: 'start_exec', index: 'start_exec', width: 100, align: "left"},
            {name: 'end_exec', index: 'end_exec', width: 100, align: "left"},
            {name: 'log', index: 'log', sortable: false}

        ],
        rowNum: 10,
        autowidth: true,
        rowList: [10],
        height: '270px',
        pager: '#pag_files',
        sortname: 'id',
        sortorder: "desc",
        hidegrid: false,
        caption: "Arquivos gerados no Projeto",
        scrollOffset: 0
    });
    $("#tab_files").jqGrid('navGrid', '#pag_files', {edit: false, add: false, del: false, search: false});

    $("#tab_files").jqGrid('setGridParam', {
        postData: {project: $('#project_id').val()},
        datatype: 'json'
    }).trigger('reloadGrid');
});