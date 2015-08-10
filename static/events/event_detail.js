$(document).ready(function(){
	$('#register-btn').on("click", function(){
		$.ajax({
			url: "/events/register/",
			success: function(data){
				console.log(data);
			}
		});
	});
});