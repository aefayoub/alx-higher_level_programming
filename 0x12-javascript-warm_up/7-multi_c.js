#!/usr/bin/node
const myarray = process.argv;
for (let i = 0; i < myarray.length; i++) {
  const number = parseInt(myarray[2]);
  if (Number.isNaN(number)) {
    console.log('Missing number of occurrences');
    break;
  } else {
    console.log('C is fun');
  }
}
