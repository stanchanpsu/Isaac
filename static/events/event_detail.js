$(document).ready(function(){
	$('#register-btn').on("click", function(){
		$.ajax({
			url: "/events/register/",
			success: function(data){
				var object = JSON.parse(data);
				if (object["registered"] === true){
					$('#status_text').text("You are registered for this event");
					$('#event_register_status').removeClass("red").addClass("teal");
					$('#register-btn').removeClass("red").addClass("teal").text("Withdraw");
				}
				else{
					$('#status_text').text("You are not registered for this event");
					$('#event_register_status').removeClass("teal").addClass("red");
					$('#register-btn').removeClass("teal").addClass("red").text("Sign up");
				}
				$("#EAs_needed").text(object["EAs_needed"] + " ambassadors needed");
			}
		});
	});
	
	$('.picture').hover(
		
		function(/*when mouseenter*/){
			
			
			
	}, 	function(/*when mouseleave */){
		
	});
});