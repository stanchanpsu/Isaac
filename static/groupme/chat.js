//define globally variable token to be used for requests
var token;
var myid;
var baseurl = "https://api.groupme.com/v3";

//instantiate token value from python which requested it from groupme during authentication
$.ajax({
    url: "/groupme/token/",
    dataType: "json",
  }).done(function(data){
    var object = JSON.parse(data);
    token = "?token=" + object['token']; // ?token=alphanumberictoken
    
    $.get(baseurl + "/users/me" + token, function(data){
      myid = data['response']['id'];
      
      groupClick();
    });
    
    
    
  });

// get list of Isaac relevant groupmegroups from django
// function getIsaacGroups(){
//   $.ajax({
//     url: "/groupme/getgroups/",
//     dataType: "json",
//   }).done(function(data){
//       var object = JSON.parse(data);
//       console.log(object);
//       return(object);
//   });
// }


//get a user's groupme groups from groupme 
function getGroupmeGroups(){
  var baseurl = "https://api.groupme.com/v3";
  $.get(baseurl +"/groups"+ token, {"per_page": 20}, function(data){
    console.log(data);
    return(data);
  });
}

function displayGroup(group_id, group_name){
  // GET /groups/:group_id/messages
  
  $.get(baseurl + "/groups/" + group_id + "/messages" + token, function(data){
    console.log(group_name, data);
    $("#header").text(group_name);
    
    var messages = [];
    
    var group_messages = data['response']['messages'].reverse();
    var length = group_messages.length;
    
    for (var i = 0; i < length; i++){
      var message = group_messages[i];
      var message_class;
      
      if (message['user_id'] == myid){
        message_class = "self";
      }
      else{
        message_class = "other";
      }
      
      var message_content = {"user_id": message['user_id'], "name": message['name'], "time": message['created_at'], "text": message['text']};
      messages[i] = '<li class =' + message_class + '><div class="avatar"><img/></div><div class="messages white-text"><p>' + message_content['text'] + '</p><time>' + message['name'] + '</time></div></li>';
    }
    
    console.log(messages);
    
    $('.discussion').empty();
    for (var user_id in messages){
      $('.discussion').append(messages[user_id]);
    }
  });
}

function groupClick(){
  $('.groups li').on("click", function(){
    var group_id = $(this).data("id");
    var group_name = $(this).text();
    displayGroup(group_id, group_name);
  });
}


// animate group panel 
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