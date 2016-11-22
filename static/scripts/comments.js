// Loads comments when page loads
$(function(){
	fetchComments();
 }); 

// Utility function: stores key and value pair
// in local storage
function setObject(key, value) {
	window.localStorage.setItem(key, JSON.stringify(value));
}

// Utility function: retrieves value from local storage based 
// on key as parameter
function getObject(key) {
	var storage = window.localStorage;
	var value = storage.getItem(key);
	return value && JSON.parse(value);
}

// Can be called from console to remove current
function clearStorage() {
	// removes everything placed in localstorage
	window.localStorage.clear();
}
	
function saveComment() {
	var cname = $('#name').val();
	var ctext = $('#comment-box').val();
	
	
	var date = new Date();
	// format date object and store in variable (DD/MM/YYYY)
	var formatted_date = date.getDate() + "/" 
		+ (date.getMonth() + 1) + "/" + 
		date.getFullYear();

	if(cname != '' || ctext != '') { // basic validation check
		var prevComments = $('#comment-area').html();
		var cmtlist = '<p><span class="comment-header">' +
			cname+' (' + 
			formatted_date + ') ' + ': ' + 
			'</span>'+ 
			ctext + '</p>';
		cmtlist += prevComments;
		$('#comment-area').empty();
		$('#comment-area').append(cmtlist);
		
		setObject('totCmts', cmtlist);
	}
}
	
function fetchComments(){
	var inlist=getObject('totCmts');
	if(inlist === null){
		inlist='';
	}
	//display the comments
	$('#comment-area').empty();
	$('#comment-area').append(inlist);
 }; 
	