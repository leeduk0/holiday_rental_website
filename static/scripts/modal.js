$(document).ready(function(){
		$( '.modal-trigger').on('click', function(e) {
		e.preventDefault();
		var image_href = $(this).attr("href");

		
		$('#modal-content').html('<img src="' + image_href + '" />');
		$('#modal-background, #modal-content').fadeIn();
	});
	
	
	$( '#modal-background').on('click', function(event) {    
		$('#modal-background, #modal-content').fadeOut();
	});

});

