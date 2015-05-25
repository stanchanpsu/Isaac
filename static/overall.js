$(document).ready(function(){
    
    LogoExpand();
    $(".button-collapse").sideNav();
    
    });

function LogoExpand(){
$("#logo").mouseenter(function(){
    var small = '20px';
    

    $(this).css({'font-size':small}).text('Integrated Schedular and Ambassador Communicator');
    }).mouseleave(function(){
        
    var big = '30px';
    $(this).css({'font-size':big}).text('Isaac');
    
    });
}
