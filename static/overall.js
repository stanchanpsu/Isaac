$(document).ready(function(){
    
    // LogoExpand();
    $(".button-collapse").sideNav();
    $(".dropdown-button").dropdown();
    $('.datepicker').pickadate({
    selectMonths: true, // Creates a dropdown to control month
    selectYears: 15 // Creates a dropdown of 15 years to control year
    });
    $('.modal-trigger').leanModal();
  
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
