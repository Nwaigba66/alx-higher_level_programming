#!/usr/bin/node
module.exports = class Rectangle {
	constructor(w, h) {
	if (w > 0 && h > 0) {
		this.width = w;
		this.height = h
	}
	}
	print() {
		const character = 'X'.repeat(this.width);
		for (let i = 0; i < this.height; i++)
		{
			console.log(character);	
		}
		}
	rotate() {
		const swap = [this.width, this.height] = [this.height, this.width];
			console.log(swap);
		}
	double() {
		const multiple = [this.width, this.height] = [this.width * 2, this.height * 2];
			console.log(multiple);
		}
};
