//define globally variable token to be used for requests
var token;
var myid;
var baseurl = "https://api.groupme.com/v3";

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');


//instantiate token value from python which requested it from groupme during authentication
$.ajax({
    url: "/groupme/token/",
    dataType: "json",
  }).done(function(data){
    var object = JSON.parse(data);
    token = object['token']; // ?token=alphanumberictoken
    
    $.get(baseurl + "/users/me?token=" + token, function(data){
      myid = data['response']['id'];
      
      groupClick();
            
    });
    
  });
  

//function to listen to clicks on groups
function groupClick(){
  $('.groups li').on("click", function(){
    var group_id = $(this).data("id");
    var group_name = $(this).text();
    displayGroup(group_id, group_name);
    sendMessagebyEnter(group_id);
  });
}

//function to display messages of a group
function displayGroup(group_id, group_name){
  
  $.get(baseurl + "/groups/" + group_id + "/messages?token=" + token, function(data){
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
    
    
    $('.discussion').empty();
    for (var user_id in messages){
      $('.discussion').append(messages[user_id]);
    }
    
    $('.discussion').scrollTop($('.discussion')[0].scrollHeight);
    
  });
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sendMessagebyEnter(group_id){
  $('#message-form').submit(function(event){
    
    
    var message = $("input:first").val();
    console.log(group_id);
    $(this).find("input[type=text]").val("");
    
    var data = {"text": message, "group_id":group_id};
    
    $.ajax({
     "beforeSend": function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    },
      "type": 'POST',
      "url": '/groupme/message/',
      "data": data,
      "complete": function(response){
        console.log(response);
      }
    });
    
    return false;
  });
}

// function sendMessagebyBtn(){
  
// }


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
  $('.groups li').on("click", function(){
    if($groups.is(":visible") && $winWidth <= 992){
      $groups.animate({
        right: -260
      }, sliderate);
    }
  });
  
  

});