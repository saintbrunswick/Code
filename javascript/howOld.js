// Write your function here:


function howOld(age, year) {
    var now = new Date()// todays date
    var currentYear = now.getFullYear()// todays year
    const birthYear = currentYear - age// birth year
    const newAge = year - birthYear// age at the future
    const underAge = year - birthYear//age in past
    const oldAge = birthYear - year//years befor was born
    if (year > currentYear || year > currentYear) {
      console.log(`You will be ${newAge} in the year ${year}`)
    } else if (year < birthYear) {
      console.log(`The year ${year} was ${oldAge} years before you were born`)
    
    } else if (year > birthYear || year < currentYear) {
      console.log(`You were ${underAge} in the year ${year}`)
    } else {
      console.log `invaid input`
    }
    }
    
    
    howOld(40, 1125);
    howOld(40, 5211);
    howOld(40, -10000);
    
    
    
  /*  
    // Once your function is written, write function calls to test your code!
    howOld(33, 2067);
    howOld(33, 1997);
    howOld(33, 87);
    
Our solution is written as a function expression and uses string interpolation, but it would be equally acceptable to use a function declaration and/or string concatenation


const howOld = (age, year) => {
    // The following two lines make it so that our function always knows the current year.
        let dateToday = new Date();
        let thisYear = dateToday.getFullYear();
    // It is totally ok if your function used the current year directly!
      
        const yearDifference = year - thisYear
        const newAge = age + yearDifference
        if (newAge < 0) {
            return `The year ${year} was ${-newAge} years before you were born`
        } else if (newAge > age) {
            return `You will be ${newAge} in the year ${year}`
        } else {
            return `You were ${newAge} in the year ${year}`
        }
    }
    */