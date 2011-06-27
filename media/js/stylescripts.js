/*

1. Why does the slidetoggle flicker? slideToggle('slow')
2. Install the maxlength plugin

*/
$(document).ready( function()
{
	jQuery('#xProb').hide();
	
	jQuery("#ViewEx").click(show_hide_xProb);
	
	var textarea = $('textarea'); 
	$('<p id="smallInfo">Characters left: <span class="charsLeft">10</span></p>').insertBefore(textarea); 
	textarea.maxlength();
	
    var $a = $("#middle");
	$a.css('margin-top', $(document).height()/2 - $a.height()/2);
	
	$('textarea').maxlength({ feedback: "p>span", hardLimit: false, words: true
	});
	
});

//show_hide_xProb controls the showing/hiding of the xProb div and the text of the "View Examples" (#ViewEx) link
function show_hide_xProb() {
	
	//if #xProb is made visible, the #ViewExlink text should say 'Hide Examples'
	if ($('#xProb').is(':visible')) {
		document.getElementById("ViewEx").innerHTML = 'View Examples';
	}
	//if #xProb is hidden, the #ViewEx link text should say 'View Examples'
	else {
		document.getElementById("ViewEx").innerHTML = 'Hide Examples';
	}
	
	$('#xProb').slideToggle();
	
	
}
	
