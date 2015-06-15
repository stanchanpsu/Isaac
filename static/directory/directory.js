var grid = "<div id='grid'></div>";

$(function(){
	$("#directory_search").on("paste keyup", function(){
		$('#grid').remove();
		$.ajax({
			url: "/directory/names/",
			data: {"term": $(this).val()},
			dataType: "json",
		}).done(function(data){
			var object = JSON.parse(data);
			console.log(data, object.length);
			$('body').append(grid);
			var i = 0;
			var row_number = 0;
			var $row = $('<div>', {id: 'row' + row_number, class: 'row'});
			$('#grid').append($row);
			for (i; i < object.length ; i++){
				var $col = $('<div>', {id: 'col' + i, class: 'col s6 l3'});
				var $card = $('<div>', {id: 'card' + i, class:'card'});
				if (i % 4 != 0 || i == 0){
					$row.append($col);
					$col.append($card);
					
					$card.append('<div class="card-image waves-effect waves-block waves-light"><img class="activator" src=' + object[i]['picture'] + '></div><div class="card-content"><span class="card-title activator grey-text text-darken-4">' + object[i]['full_name'] + '<i class="mdi-navigation-more-vert right"></i></span><p>' + object[i]['major'] + '</p></div><div class="card-reveal"><span class="card-title grey-text text-darken-4">' + object[i]['full_name'] + '<i class="mdi-navigation-close right"></i></span><p>Here is some more information about this product that is only revealed once clicked on.</p><a href="">Profile</a></div>');
				}
				else if ( i % 4 == 0 && i !=0 ){
					$row.append($col);
					$col.append($card);
					
					$card.append('<div class="card-image waves-effect waves-block waves-light"><img class="activator" src=' + object[i]['picture'] + '></div><div class="card-content"><span class="card-title activator grey-text text-darken-4">' + object[i]['full_name'] + '<i class="mdi-navigation-more-vert right"></i></span><p>' + object[i]['major'] + '</p></div><div class="card-reveal"><span class="card-title grey-text text-darken-4">' + object[i]['full_name'] + '<i class="mdi-navigation-close right"></i></span><p>Here is some more information about this product that is only revealed once clicked on.</p><a href="">Profile</a></div>');
					
					$('#grid').append($row);
					row_number++;
				}
				// $('#card' + i).append("<div class='card-image waves-effect waves-block waves-light'><img class='activator src=" + object[i]['picture'] + "></div><div class='card-content'><span class='card-title activator grey-text text-darken-4'>" + object[i]['full_name'] + "<i class='mdi-navigation-more-vert right'></i></span><p>" + object[i]['major'] + "</p></div><div class='card-reveal'><span class='card-title grey-text text-darken-4'>" + object[i]['full_name'] + "<i class='mdi-navigation-close right'></i></span><p>Here is some more information about this product that is only revealed once clicked on.</p><a href=''>Profile</a></div>");
			}
		});
	});
});