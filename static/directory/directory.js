$(function() {
	$("#directory_search").on("paste keyup", function() {
		$.ajax({
			url: "/directory/names/",
			data: {"term": $(this).val()},
			dataType: "json",
		}).done(function(data){
			console.log(data);
		});
	});
});