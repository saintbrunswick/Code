// Write your function here:

function finalGrade(midterm, final, homework) {
  let average = ((midterm + final + homework)/3);
  //average = average / 3;
    if (average <= 1 || average <= 59) {
      return "F"
    } else if (average <= 60 || average <= 69) {
      return "D"
    } else if (average <= 70 || average <= 79) {
      return "c"
    } else if (average <= 80 || average <= 89) {
      return "B"
    } else if (average <= 90 || average <= 100) {
      return 'A'
    } else (average <= 0 || average > 100) 
      return 'You have entered an invalid grade'
    };
  

//console.log(finalGrade(0, 0, 0))// print invalid
// Uncomment the line below when you're ready to try out your function
 console.log(finalGrade(99, 92, 95)) // Should print 'A'

// We encourage you to add more function calls of your own to test your code!