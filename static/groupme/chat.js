$(function(){
  var $discussion = $('.discussion-div');
  var $form = $('form');
  var $activate = $("#activate-groups");
  var $groups = $('.groups'); 
  var $winWidth = $(window).width();
  var token;
    
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
    });
  });
  
  //event listeners for click of the discussion or form (message input) to close the group panel if it is open
  $discussion.on("click", function(){
    if($groups.is(":visible") && $winWidth <= 992){
      $groups.animate({
        right: -260
      });
    }
  });
  $form.on("click", function(){
    if($groups.is(":visible") && $winWidth <= 992){
      $groups.animate({
        right: -260
      });
    }
  });
  
  //get the groupme access token from django view
  $.ajax({
    url: "/groupme/token/",
    dataType: "json",
  }).done(function(data){
    var object = JSON.parse(data);
    token = object['token'];
  });
  
  
});