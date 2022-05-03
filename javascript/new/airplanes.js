let Airplane = {}
Airplane.myAirplane = "StarJet"
module.exports = Airplane;
console.log(module.export = Airplane)


const Airplane = require('./1-airplane.js')

function displayAirplane() {
console.log(Airplane.myAirplane);
} 
displayAirplane()

/*let availableAirplanes = [{
 name: 'AeroJet',
 fuelCapacity: 800,
 availableStaff: ['pilots', 'flightAttendants', 'engineers', 'medicalAssistance', 'sensorOperators'],
}, 
{name: 'SkyJet',
 fuelCapacity: 500,
 availableStaff: ['pilots', 'flightAttendants']
}];

let flightRequirements = {
  requiredStaff: 4,
};

function meetsStaffRequirements(availableStaff, requiredStaff) {
  if (availableStaff.length >= requiredStaff) {
    return true;
  } else {
    return false;
  }
};

export { availableAirplanes, flightRequirements, meetsStaffRequirements};

let Airplane = {
};
Airplane.availableAirplanes = [
  {
  name: 'AeroJet', 
  fuelCapacity: 800,
  },
  {
name: 'SkyJet', 
fuelCapacity: 500
  }
];
export default Airplane;

console.log(Airplane)
















*/