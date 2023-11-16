#!/usr/bin/node

let bigest = 0;
let i;
const array = [];

for (i = 2; i < process.argv.length; i++) {
  if (Number.isNaN(parseInt(process.argv[i])) === false) {
    array[i - 2] = parseInt(process.argv[i]);
  }
}

if (array.length > 1) {
  bigest = Math.max.apply(null, array);
  i = array.indexOf(bigest);
  array[i] = -Infinity;
  bigest = Math.max.apply(null, array);
}

console.log(bigest);
