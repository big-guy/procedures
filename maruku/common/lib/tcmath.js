// When the page is ready
$(document).ready(function () {
   function linkTo(tc) {
      return "<a href='#test_case_" + tc + "'>" + tc + "</a>";
   }

   function casesWithValue(value) {
      var links = []
      $(':radio[value=' + value + ']:checked').each(function() {
         var tc = $(this).attr('name').slice(2)
         links.push(linkTo(tc))
      })
      return links 
   }

   function prettyPrintCasesWithValue(value) {
      var cases = casesWithValue(value)
      var total = totalCases()
      var percentage = Math.round(cases.length*100/total)

      var links = ""
      var i, len
      for (i=0, len=cases.length; i<len; ++i) {
         links += (cases[i] + " ")
      }

      return cases.length + " (" + percentage + "%) " + links
   }

   function totalCases() {
      var totalTestCases=$('input[type="radio"]:checked').length
      return totalTestCases
   }

   $('td#passed_cases').html(prettyPrintCasesWithValue("Pass"))
   $('td#failed_cases').html(prettyPrintCasesWithValue("Fail"))
   $('td#skipped_cases').html(prettyPrintCasesWithValue("Skip"))
   $('td#total_cases').text(totalCases())
});
