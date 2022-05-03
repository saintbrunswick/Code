let raceNumber = Math.floor(Math.random() * 1000);
//runner was registered early
const registeredEarly = true;
//Age of racer
const age = 15;
//Racer is an adult
if (age > 18) {
  raceNumber = (raceNumber + 1000);
} else if (age < 18) {
  raceNumber
 } else if (age === 18) {
   console.log(`See the registration desk.`);
}

if ( raceNumber < 1000) {
  console.log(`Youth registrants run at 12:30 pm (regardless of registration) ${raceNumber}`);
} else if (registeredEarly === true && raceNumber >= 1000) {
  console.log(`Early adults run at 9:30am ${raceNumber}`);
} else if (registeredEarly === false && raceNumber >= 1000) {
  console.log(`Late adults run at 11:00 am ${raceNumber}`)
};
