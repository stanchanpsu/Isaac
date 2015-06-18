//instantiate the grid div
var grid = "<div id='grid'></div>";


//custom function from StackOverflow to sort any Json Object by any key in forward or reverse direction (reverse arg3 = -1)
function sortJsonArrayByProperty(objArray, prop, direction){
    if (arguments.length<2) throw new Error("sortJsonArrayByProp requires 2 arguments");
    var direct = arguments.length>2 ? arguments[2] : 1; //Default to ascending

    if (objArray && objArray.constructor===Array){
        var propPath = (prop.constructor===Array) ? prop : prop.split(".");
        objArray.sort(function(a,b){
            for (var p in propPath){
                if (a[propPath[p]] && b[propPath[p]]){
                    a = a[propPath[p]];
                    b = b[propPath[p]];
                }
            }
            // convert numeric strings to integers
            a = a.match(/^\d+$/) ? +a : a;
            b = b.match(/^\d+$/) ? +b : b;
            return ( (a < b) ? -1*direct : ((a > b) ? 1*direct : 0) );
        });
    }
}

// main function that is self calling
$(function ajax_query(){
	// on change, paste, or keyup within the directory search bar
	$("#directory_search").on("change paste keyup", function(){
		//ajax request /directory/names/ for a json with the search value as a query "term"
		$.ajax({
			url: "/directory/names/",
			data: {"term": $(this).val()},
			dataType: "json",
			// on return of the data
		}).done(function(data){
			console.log(data); // for debugging
			// remove the current grid div containing all the cards
			$('#grid').remove();
			// parse the data as a json and store it in object
			var object = JSON.parse(data);
			sortJsonArrayByProperty(object, 'full_name');
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
			for (i; i < object.length; i++){
				//instantiate a column div and card div as well as the ambassador card which uses dynamic data for each person
				var $col = $('<div>', {id: 'col' + i, class: 'col s6 l3'});
				var $card = $('<div>', {id: 'card' + i, class:'card'});
				// note: the javascript string marker quotation must be single quote and the html quotes must be double quote because the json returned by django stores strings as double quotes
				var ambassador_card = '<div class="card-image waves-effect waves-block waves-light"><img class="activator" src=' + object[i]['picture'] + '></div><div class="card-content"><span class="card-title activator grey-text text-darken-4">' + object[i]['full_name'] + '<i class="mdi-navigation-more-vert right"></i></span><p>' + object[i]['major'] + '</p></div><div class="card-reveal"><span class="card-title grey-text text-darken-4">' + object[i]['full_name'] + '<i class="mdi-navigation-close right"></i></span><a href="/directory/' + object[i]['id'] + '" class="waves-effect waves-light btn blue">Profile<i class="mdi-social-person left"></i></a><p>' + object[i]['aboutme'] + '</p></div>';
				
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