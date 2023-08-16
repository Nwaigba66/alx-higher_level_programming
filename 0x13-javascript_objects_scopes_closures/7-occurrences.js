#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let Count = 0;
  list.forEach(element => {
    if (element === searchElement) {
      Count++;
    }
  });

  return Count;
};
