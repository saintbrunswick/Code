//Kelvin temperature = 293 C
const kelvin = 0;
//Celsius temperature is 273 degrees lover than Kelvin
let celsius = kelvin - 273;
/*Farenheight substraction from Celsius.
Rounded number.*/
let fahrenheit = Math.floor(celsius * (9/5) + 32);
/*Newton converted from Celsius.
Rounded number.*/
let newton = Math.floor(celsius * (33/100));
console.log('The temperature is ' + fahrenheit + ' degrees Fahrenheith.');
console.log('The temperature is ' + kelvin + ' degrees Kelvin.');
console.log('The temperature is ' + celsius + ' degrees Celsius.');
console.log('The temperature is ' + newton + ' degrees Newton.')