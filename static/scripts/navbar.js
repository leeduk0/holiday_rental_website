$(document).ready(function() {
	// When 3 line icon is clicked
	$('.menu-trigger').on('click', function() {

		$("nav ul").slideToggle(500);
	});
	
	// Makes sure nav bar is reset when window is resized
	// and after toggling at least once
	$(window).resize(function(){
		var w = $(window).width();
		if(w > 780 && $('nav ul').is(':hidden')) {
			$('nav ul').removeAttr('style');
		}
});

});