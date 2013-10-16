// When the page is ready
$(document).ready(function () {
/*   function(type) {
      $('input[type=radio]').each { 
         alert($(this))
      }
   } */
   function linkTo(tc) {
      return "<a target='_self' href='#test_case_" + tc + "'>" + tc + "</a>";
   }

   $('td#passed_cases').text("0 (0%)")
   $('td#failed_cases').text("0 (0%)")
   $('td#skipped_cases').html("12 (100%) " + linkTo(1) + " 2 3 4 5 6 7 8 9 10 11 12")
   $('td#total_cases').text("12")
});
