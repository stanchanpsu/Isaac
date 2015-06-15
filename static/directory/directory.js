//instantiate the grid div
var grid = "<div id='grid'></div>";

// main function that is self calling
$(function(){
	// on change, paste, or keyup within the directory search bar
	$("#directory_search").on("change paste keyup", function(){
		//ajax request /directory/names/ for a json with the search value as a query "term"
		$.ajax({
			url: "/directory/names/",
			data: {"term": $(this).val()},
			dataType: "json",
			// on return of the data
		}).done(function(data){
			// remove the current grid div containing all the cards
			$('#grid').remove();
			// parse the data as a json and store it in object
			var object = JSON.parse(data);
			// append a new grid div to the body
			$('body').append(grid);
			// instantiate counting variables
			var i = 0;
			var row_number = 0;
			//instantiate a row div
			var $row = $('<div>', {id: 'row' + row_number, class: 'row'});
			//append it to the grid
			$('#grid').append($row);
			// for every ambassador within the object json data
			for (i; i < object.length ; i++){
				//instantiate a column div and card div as well as the ambassador card which uses dynamic data for each person
				var $col = $('<div>', {id: 'col' + i, class: 'col s6 l3'});
				var $card = $('<div>', {id: 'card' + i, class:'card'});
				// note: the javascript string marker quotation must be single quote and the html quotes must be double quote because the json returned by django stores strings as double quotes
				var ambassador_card = '<div class="card-image waves-effect waves-block waves-light"><img class="activator" src=' + object[i]['picture'] + '></div><div class="card-content"><span class="card-title activator grey-text text-darken-4">' + object[i]['full_name'] + '<i class="mdi-navigation-more-vert right"></i></span><p>' + object[i]['major'] + '</p></div><div class="card-reveal"><span class="card-title grey-text text-darken-4">' + object[i]['full_name'] + '<i class="mdi-navigation-close right"></i></span><p>Here is some more information about this product that is only revealed once clicked on.</p><a href="">Profile</a></div>';
				
				// if the card is not the end of a row or it is the first card
				if (i % 4 != 0 || i == 0){
					// just append the column, card, and ambassador card divs
					$row.append($col);
					$col.append($card);
					$card.append(ambassador_card);
				}
				// else if the end of a column but not the first card
				else if ( i % 4 == 0 && i !=0 ){
					// increment the row counter
					row_number++;
					// redefine the row div and append it along with the column, card, and ambassador card.
					$row = $('<div>', {id: 'row' + row_number, class: 'row'});
					$('#grid').append($row);
					$row.append($col);
					$col.append($card);
					$card.append(ambassador_card);
				}
			}
		});
	});
});