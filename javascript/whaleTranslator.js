let input = 'a whale of a deal!';
const vowels = ['a', 'e', 'i', 'o', 'u'];
let resultArray = [];
for (let i = 0; i < input.length; i++) {
 
  for (let j = 0; j < vowels.length; j++) {
  //console.log('i is '+ i);
  //console.log('j is '+ j);
  if (i === j) {
    resultArray.push(vowels[j]);
  } else if (input[i] === 'e' || input[i] === 'u') {
  resultArray.push(input[i]);
  }
  }
}
console.log(resultArray.toString());
console.log(resultArray.join('').toUpperCase());