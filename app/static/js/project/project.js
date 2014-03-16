/**
 *  Created by erick on 3/16/14.
 */


$(document).ready(function () {

    function actions(cellValue, options, rowObject) {
        debug(cellValue);
        debug(options);
        debug(rowObject)

        var view = '<button class="btn-view mini open" title="Visualizar registro." data-url="/app/project/view/' + rowObject.id + '.html"></button>';
        var table = '<button class="btn-table mini open" title="Tabelas do Projeto" data-url="/app/project/view/' + rowObject.id + '.html"></button>';
        var edit = '<button class="btn-edit mini open" title="Editar Projeto" data-url="/app/project/view/' + rowObject.id + '.html"></button>';
        var trash = '<button class="btn-trash mini open" title="Excluir Projeto" data-url="/app/project/view/' + rowObject.id + '.html"></button>';
        return view + table + edit + trash;
    }

    $("#tab_project").jqGrid({
        url: '/app/project/search.html',
        datatype: "json",
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
        pager: '#pag_project',
        sortname: 'id',
        viewrecords: true,
        sortorder: "asc",
        hidegrid: false,
        caption: "Resultado da pesquisa",
        scrollOffset: 0,
        jsonReader: { repeatitems: false }
    });
    $("#tab_project").jqGrid('navGrid', '#pag_project', {edit: false, add: false, del: false, search: false});
});
