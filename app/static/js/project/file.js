$(document).ready(function () {

    function file_actions(cellValue, options, rowObject) {

        var files = '';

        if (rowObject.status == 'Concluído') {
            files += '<a class="btn-files mini" ' +
                'title="Arquivos Gerados"' +
                'target="_blank" ' +
                'href="/media/' + rowObject.file + '"' +
                'disabled="true"></a>';
        }

        return files;
    }

    $("#tab_files").jqGrid({
        url: '/app/project/files/search.html',
        datatype: 'json',
        colNames: ['Ações', 'Código', 'Data criação', 'Situação'],
        colModel: [
            {name: 'actions', width: 100, formatter: file_actions, align: "center", sortable: false},
            {name: 'id', index: 'id', width: 80, align: "center", key: true},
            {name: 'created', index: 'created', width: 80, align: "center", key: true},
            {name: 'status', index: 'status', width: 80, align: "center"}
        ],
        rowNum: 10,
        autowidth: true,
        rowList: [10],
        height: 'auto',
        minHeight: '270px',
        pager: '#pag_files',
        sortname: 'id',
        sortorder: "asc",
        hidegrid: false,
        caption: "Arquivos gerados no Projeto",
        scrollOffset: 0
    });
    $("#tab_files").jqGrid('navGrid', '#pag_files', {edit: false, add: false, del: false, search: false});


});