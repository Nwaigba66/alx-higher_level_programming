#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const lastNumber = list.length - 1;
  for (let n = lastNumber; n >= 0; n--) {
    newList.push(list[n]);
  }
  return newList;
};
