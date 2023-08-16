#!/usr/bin/node
const BaseSquare = require('./5-square.js');
class Square extends BaseSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      const symbol = c.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(symbol);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
