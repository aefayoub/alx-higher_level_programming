#!/usr/bin/node
const lenArray = parseInt(process.argv[2]);
if (Number.isNaN(lenArray)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < lenArray; i++) {
    console.log('C is fun');
  }
}
