/*
MIT License
Copyright 2014 Sterling Greene
*/

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
      for (i=0, len=Math.min(cases.length, 12); i<len; ++i) {
         links += (cases[i] + " ")
      }
      if (i!=cases.length) {
         links += " ..."
      }

      return cases.length + " (" + percentage + "%) " + links
   }

   function totalCases() {
      var totalTestCases=$('input[type="radio"]:checked').length
      return totalTestCases
   }

   function updateProgress() {
      $('td#passed_cases').each(function() { $(this).html(prettyPrintCasesWithValue("Pass")) })
      $('td#failed_cases').each(function() { $(this).html(prettyPrintCasesWithValue("Fail")) })
      $('td#skipped_cases').each(function() { $(this).html(prettyPrintCasesWithValue("Skip"))})
      $('td#total_cases').text(totalCases())
   }

   function coveredRequirement() {
      $('dt').each(function() { 
      	// var id = $(this).attr('id')
        if ($('a[href="#' + this.id + '"]').size() == 0) {
           $(this).addClass('notcovered')
	   $(this).append(' - Requirement not covered!')
        } else {
           $(this).addClass('covered')
	}
      })
   }
   coveredRequirement()
   updateProgress()
   setInterval(updateProgress, 5000)
});
