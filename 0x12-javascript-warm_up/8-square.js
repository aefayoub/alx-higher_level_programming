#!/usr/bin/node
const lenArray = parseInt(process.argv[2]);
if (Number.isNaN(lenArray)) {
  console.log('Missing size');
} else {
  for (let i = 0, x; i < lenArray; i++) {
    x = '';
    for (let j = 0; j < lenArray; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
