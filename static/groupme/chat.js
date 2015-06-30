//define globally variable token to be used for requests
var token;

//instantiate token value from python which requested it from groupme during authentication
$.ajax({
    url: "/groupme/token/",
    dataType: "json",
  }).done(function(data){
    var object = JSON.parse(data);
    token = object['token'];
    
    // get groups
    var GroupmeGroups = getGroupmeGroups();
    var IsaacGroups = getIsaacGroups();
    
    //a place to store only isaac relevant group ids
    var GroupIDs = [];
    
    // fill GroupIDs by iterating through Isaac Groups
    for (var group in IsaacGroups){
      GroupIDs.push(IsaacGroups[group]['fields']['group_id']);
    }
    
    console.log(GroupIDs);
    console.log(IsaacGroups);
    
    
  });

// get list of Isaac relevant groupmegroups from django
function getIsaacGroups(){
  $.ajax({
    url: "/groupme/getgroups/",
    dataType: "json",
  }).done(function(data){
      var object = JSON.parse(data);
      console.log(object);
      return(object);
  });
}


//get a user's groupme groups from groupme 
function getGroupmeGroups(){
  var baseurl = "https://api.groupme.com/v3";
  $.get(baseurl +"/groups?token="+ token, {"per_page": 20}, function(data){
    console.log(data);
    return(data);
  });
}

$(function(){
  var $discussion = $('.discussion-div');
  var $form = $('form');
  var $activate = $("#activate-groups");
  var $groups = $('.groups'); 
  var $winWidth = $(window).width();
  var sliderate = 300;
    
    //initialize page with activate buttom showing if mobile and groups hidden to the right by 260px (width of panel)
    if ($winWidth <= 992){
      $activate.show();
      $groups.css("right", -260);
    }
    //opposite if not mobile
    else if ($winWidth > 992){
      $activate.hide();
      $groups.css("right", 0);
    }
  
  //listen for resize of window and do the same things as above
  $(window).resize(function(){
    $winWidth = $(window).width();
    
    if ($winWidth <= 992){
      $activate.show();
      $groups.css("right", -260);
    }
    else if ($winWidth > 992){
      $activate.hide();
      $groups.css("right", 0);
    }
  });
  
  //event listener for click of activate button to animate in groups panel  
  $activate.on("click", function(){
    $groups.animate({
      right: 0
    }, sliderate);
  });
  
  //event listeners for click of the discussion or form (message input) to close the group panel if it is open
  $discussion.on("click", function(){
    if($groups.is(":visible") && $winWidth <= 992){
      $groups.animate({
        right: -260
      }, sliderate);
    }
  });
  $form.on("click", function(){
    if($groups.is(":visible") && $winWidth <= 992){
      $groups.animate({
        right: -260
      }, sliderate);
    }
  });

});