#!/usr/bin/node

function findSecondBiggestInt (integers) {
  if (integers.length === 0 || integers.length === 1) {
    return 0;
  }
  integers.sort((a, b) => a - b); // Sort in ascending order

  return integers[integers.length - 2]; // Return second-to-last element
}
console.log(findSecondBiggestInt(process.argv.slice(2)));
