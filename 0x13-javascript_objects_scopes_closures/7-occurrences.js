#!usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let n = 0;
  while (n < list.length) {
    if (list[n] === searchElement) {
      count++;
    }
    n++;
  }
  return count;
};
