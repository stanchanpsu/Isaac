$(document).ready(function(){
	$('#register-btn').on("click", function(){
		$.ajax({
			url: "/events/register/",
			success: function(data){
				var object = JSON.parse(data);
				
				var figure = '<div id="' + object["me-id"] +  '" ' + 'class="figure"><a id="' +object["me-id"] + '-link"  href="/directory/' + object["me-id"] + '"></a></div>';
				
				var $me = $('<img>', {
					class: "z-depth-1 picture",
					src: object["me-url"],
					alt: object["me"],
				});
				
				var caption = '<figcaption>' + object["me"] + '</figcaption>'
								
				if (object["registered"] === true){
					$('#status_text').text("You are registered for this event");
					$('#event_register_status').removeClass("red").addClass("teal");
					$('#register-btn').removeClass("red").addClass("teal").text("Withdraw");
					$('#eas').append(figure);
					$('#' + object["me-id"] + '-link').append($me).append(caption);
					
				}
				else if (object["registered"] === false && object["EAs_needed"] > 0){
					$('#status_text').text("You are not registered for this event");
					$('#event_register_status').removeClass("teal").addClass("red");
					$('#register-btn').removeClass("teal").addClass("red").text("Sign up");
					$('#' + object["me-id"]).remove();
				}
				else{
					$('#register-btn').text("No EAs Needed");
				}
				$("#EAs_needed").text(object["EAs_needed"] + " ambassadors needed");
			}
		});
	});
});