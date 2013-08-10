$(document).ready(function() {
	$('#create-conection').button();

	$('#create-conection').on('click', function() {
		$('.window').dialog({
			modal : true
		});
	});
});