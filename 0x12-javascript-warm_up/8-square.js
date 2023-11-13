#!/usr/bin/node
const lenArray = parseInt(process.argv[2]);
if (Number.isNaN(lenArray)) {
  console.log('Missing size1');
} else {
  for (let i = 0; i < lenArray; i++) {
    x = '';
    for (let j = 0; j < lenArray; j++) {
      x += 'x';
    }
      console.log(x);
  }
}
