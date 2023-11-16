#!/usr/bin/node
function factorial (arg) {
  if ((Number.isNaN(arg)) || (arg === 1)) {
    return 1;
  }
  return factorial(arg - 1) * arg;
}

console.log(factorial(parseInt(process.argv[2])));
